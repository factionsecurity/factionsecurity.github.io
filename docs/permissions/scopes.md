---
description: "The scope tiers in OWASP Faction permissions, from all records down to a single assessment, and how each one is resolved at runtime."
---

# Scopes

The scope segment decides which records a permission reaches. Tiers are **mutually exclusive and
ordered** — a resolver checks them widest-first and the first match wins, so a role holding both
`assessments:read:all` and `assessments:read:team` is simply an all-scope role.

| Scope | Reaches | Resolved from |
| --- | --- | --- |
| `all` | every record in the system | the permission alone |
| `org` | records in the caller's own organization | `User.organizationId` |
| `owned` | applications assigned to the caller, or their whole org when they have no application-level assignments | `Application.assignedUsers`, else the home org |
| `team` | records whose assessment belongs to one of the caller's teams | `Assessment.teamId` ∈ `User.teamIds` |
| `assigned` | assessments the caller is an assessor on | `Assessment.assessorIds` (or the legacy `assessorId`) |
| `assessment` | the records of assessments the caller can reach | borrows the caller's assessment scope |
| `self` | the caller's own records (API keys) | the authenticated user |
| `system` | ownerless service-account records (API keys) | n/a |

## The resolvers

**`AccessScopeService.resolveAssessmentScope`** turns the caller's authorities into an
`AssessmentScope` — `UNRESTRICTED`, `ORG`, `OWNED`, `TEAM`, `ASSIGNED`, or `DENIED`. The list
query applies it as SQL filters and `AssessmentScope.permits()` applies the same rule to a single
record, so a list and a direct fetch can never disagree. A caller with **no** assessment read
authority resolves to `DENIED` and sees nothing.

`resolveAssessmentEditScope` and `resolveAssessmentDeleteScope` are separate on purpose: "see the
whole team's work, edit only your own" is a common setup, and deleting is a third grant again — a
scheduler may delete their team's bookings without being able to edit anyone's findings. All three
produce the same `AssessmentScope` type, so a tier means the same thing whichever verb resolved it.

**`VulnerabilityScopeResolver`** does the same for cross-assessment vulnerability queries — the
vulnerabilities list, the severity summary, and the remediation queue. Its `:assessment` tier
delegates to the assessment scope above rather than defining its own notion of reachability, so
"the assessments I can open" and "the findings I can see" cannot drift apart.

One behavior to be aware of: a caller holding **no** vulnerability read scope at all is treated
as unrestricted by this resolver rather than denied, which is the opposite of the assessment
resolver's default. The endpoint gate is what stops an unauthorized caller there.

## Scope is per resource

A wide grant on one resource does not widen another. `applications:read:all` says nothing about
which *users* you may see; only a `users:*:all` grant does that.

!!! warning "This was a real bug"
    `UserService` used to test `authority.contains(":all")` when deciding whether a caller could
    reach every user. Any unrelated `:all` grant — `applications:read:all`, which every pentester
    role carries — silently turned `users:read:team` into unrestricted access to every user in
    the system. It now matches the four `users:*:all` strings exactly. If you write a similar
    check, compare exact strings.

## Team scope depends on the assessment's team

`team` resolves against `Assessment.teamId`, which is **optional** when an assessment is created.
An assessment saved without a team belongs to no team and is invisible to every team-scoped user,
and a team-scoped caller who belongs to no team sees nothing at all (the query becomes
`AND 1 = 0` rather than falling open).

Peer review is the exception: it derives an assessment's teams from its *assessors'* team
membership rather than from `Assessment.teamId`. The same assessment can therefore be in scope
for peer review and out of scope for the assessment list.

## API key scopes

API keys use `self` and `system`, and deliberately have **no** `all` tier.

- `apikeys:{create,read,delete}:self` — your own keys. Every user-key endpoint is self-scoped;
  there is no surface for managing another user's keys, so an unscoped grant would imply a
  capability that does not exist.
- `apikeys:{read,delete}:system` — the delegable half of service-account key management.
- Minting or re-scoping a **system** key is `super_admin` only, with no permission string at all.
  A system key can carry any authority, so a delegable create would let a caller grant authority
  they do not hold. That invariant — a key never confers more than its creator has — is why
  there is no `apikeys:create:system` to check in the Roles matrix.
