---
description: "The built-in roles in OWASP Faction and the permissions each one grants."
---

# Built-in roles

`BootstrapService` seeds these on startup. The seeding is **idempotent and additive**: a role
that already exists keeps any permission an administrator added on top, and only gains ones it is
missing. A seeded role that has been deleted is recreated on the next boot.

Two roles are protected from deletion in `RoleService`: **SuperAdmin** and **Pentester**.

## Internal roles

### SuperAdmin

A single permission, `super_admin`, which is implied by every gate and bypasses every scope
resolver. It is not part of the assignable catalog, so it cannot be granted from the Roles screen
and is not copied when a role is duplicated.

### Pentester

The default role for internal testers, and the one the seeded `pentest` user gets. Assessments
are **assigned-only**: a pentester sees and edits the assessments they are an assessor on.

- `assessments:read:assigned`, `assessments:edit:assigned`, `assessments:create:team`
- `vulnerabilities:{read,create,edit,delete}:assessment`
- `applications:read:all`
- `organizations:{read,create,edit,delete}:all` — Organizations lives under Administration and
  pentesters run it
- `peerreview:{read,edit,create}:all`
- `reporting:create`, `reporting:download`
- `report_templates:{read,create,edit,delete}:all` — the Report Designer is reachable on
  `assessments:create:team`, but every call the page makes is gated on these four, so without
  all of them the page opens onto a 403
- `apikeys:{create,read,delete}:self`

!!! note "One permission is actively revoked"
    Startup removes `assessments:read:team` from this role. It was seeded back when no code
    enforced the tier, so it was indistinguishable from "read everything". Now that the tiers are
    enforced the default is assigned-only. Re-grant it from the Roles screen for teams that want
    the team-wide view — the revocation only runs against the seeded default.

### Pentester-Team

The same work, scoped to the tester's teams. Everything it reaches is bounded by
`Assessment.teamId` ∈ the user's `teamIds`.

- `assessments:{read,edit,create}:team`
- `vulnerabilities:{read,create,edit,delete}:team`
- `peerreview:{read,edit}:team`, `peerreview:create:assessment`
- `applications:read:all`, `reporting:create`, `reporting:download`, `apikeys:*:self`

### Pentester-Assessment

Scoped to the assessments the tester is assigned to. Assessments have no `:assessment` tier —
`:assigned` is that tier for them.

- `assessments:{read,edit}:assigned`
- `vulnerabilities:{read,create,edit,delete}:assessment`
- `peerreview:create:assessment`
- `applications:read:all`, `reporting:create`, `reporting:download`, `apikeys:*:self`

!!! warning "What the two scoped roles deliberately lack"
    Neither carries `organizations:*:all` or `report_templates:*:all`, so **Organizations admin
    and the Report Designer are unavailable** to them. `Pentester-Assessment` also has no
    `assessments:create:*`, so it cannot schedule new work at all. `applications:read:all` stays
    on both because every assessment view resolves its application and no `:team` application
    permission exists to narrow it to.

    Startup also revokes `peerreview:{read,edit,create}:all` from both, so a database seeded
    before the team-scoped peer-review grants tightens rather than keeping org-wide access.

## Remediation roles

For people who track findings to closure without running assessments. Both are seeded with the
same additive contract as the Pentester roles.

### Remediation-Team

Remediation across the user's teams.

- `assessments:read:team`
- `vulnerabilities:{read,create,edit,delete}:team`
- `applications:read:all`, `organizations:read:all`

### Remediation-All

The same work with no scope — every assessment's findings and retests.

- `assessments:read:all`
- `vulnerabilities:{read,create,edit,delete}:all`
- `applications:read:all`, `organizations:read:all`

!!! info "Why the lists are shorter than the descriptions"
    Two of the advertised capabilities have no permission string of their own:

    - **Commenting** is gated on the vulnerability *read* family. The
      `vulnerabilities:comment:*` strings exist only in `:org` / `:owned` form, for portal users,
      so an internal role comments by virtue of `vulnerabilities:read:{team,all}`.
    - **Retests** reuse the vulnerability verbs at the same tier — `RetestController` gates
      create/read/edit/delete on `vulnerabilities:{create,read,edit,delete}:*`.

    `assessments:read:*` is likewise not optional, and not decoration: every single-vulnerability
    operation runs through `checkAssessmentAccess`, and a caller with no assessment read grant
    resolves to `DENIED`. Without it the queue lists findings that 403 the moment one is opened.
    The grant is deliberately read-only — remediation tracks findings, it does not edit the
    assessment around them.

    `applications:read:all` and `organizations:read:all` feed the queue's filter dropdowns, and
    neither endpoint offers a narrower tier.

## Scheduling roles

For the people who book the work rather than perform it. Two tiers only: unscoped and team.

### Scheduling

- `assessments:{read,create,edit,delete}:all`
- `users:read:all`
- `applications:{read,create,edit}:all`
- `organizations:{read,create,edit}:all`
- `campaigns:{read,create,edit}:all`
- `checklist:create`, `checklist:edit`
- `report_templates:read:all`

### Scheduling-Team

The same, narrowed to the scheduler's own teams:

- `assessments:{read,create,edit,delete}:team`
- `users:read:team` — `UserService` filters the assessor picker to shared teams
- everything else identical to **Scheduling**

!!! info "Why the team role still holds `:all` permissions"
    Applications, organizations, and campaigns define **no** `:team` tier — only org-wide
    variants (plus `:org`/`:owned` for portal users). A team-scoped scheduler therefore still
    books against the whole application and organization catalog. If that is too wide for your
    install, the fix is a new scope tier in the enum and a resolver to enforce it, not a
    different role.

    `report_templates:read:all` is a read, not an authoring grant: the scheduling form loads the
    templates available for the chosen assessment type, and that endpoint is gated on it — without
    it the picker 403s mid-form. Create/edit/delete of templates stay with the Pentester role.

    `assessments:create:team` is not team-validated — see
    [What is enforced](enforcement.md#gate-only-the-permission-opens-the-door-and-nothing-narrows-it).
    A `Scheduling-Team` holder can book an assessment onto another team, or onto none, even though
    everything they read is team-bounded.

    Deletion is limited to assessments — neither role can delete an application, organization,
    campaign, or template — and it is scoped: `Scheduling-Team` deletes only its own teams'
    assessments, enforced by `resolveAssessmentDeleteScope`. Neither role runs assessments or
    reads vulnerabilities.

!!! note "Team reads accept the team tier"
    `GET /teams` and its two sibling reads were gated on `users:read:all` alone, which left
    `Scheduling-Team` unable to load the team picker — the field every team scope resolves
    against. They now accept `users:read:team` as well. Creating, editing, and deleting teams,
    and moving users between them, remain `super_admin` only.

## External roles

Marked `externalRole`, which is what makes them assignable to portal (client) users.

### Organization Read

Read-only access to the caller's own organization: `organizations:read:org`,
`applications:read:org`, `vulnerabilities:read:org`, `assessments:read:org`.

### App Owner

Scoped to assigned applications. With no application-level assignment the user falls back to
their whole home organization; with one, they see only those applications, and may edit an
application only where their assignment is `WRITE`.

- `applications:read:owned`, `applications:create:owned`, `organizations:read:owned`
- `assessments:read:owned`, `vulnerabilities:read:owned`
- `vulnerabilities:comment:owned`, `vulnerabilities:retest:owned`
- `reporting:download:owned`, `survey:complete`

## Which dashboard a role lands on

`Dashboard.tsx` routes on role **name**, not on permissions: `super_admin` authorities get the
super-admin dashboard, any role named `Pentester` or starting with `Pentester-` gets the pentester
dashboard, `App Owner` gets the app-owner dashboard, a role named `Remediation` or starting with `Remediation-` gets the vulnerability
dashboard, and anything holding `manager_dashboard:read:all` is redirected to the operational
dashboard. A custom role named something else falls through to a generic placeholder however its
permissions are set — worth knowing before renaming a seeded role.

The Remediation roles reach the vulnerability dashboard on the permissions they already hold:
its summary endpoint accepts `vulnerabilities:read:{all,team}`, and its organization and
sub-organization filters are gated on `organizations:read:all`. The Remediation page at
`/remediation` and its sidebar badge are likewise satisfied by `vulnerabilities:read:{all,team}`.

## Creating a role from an existing one

The Roles screen has a **Duplicate** action on each row: it opens the create form pre-filled with
the source role's permissions, description, and external flag, named `<Name> (Copy)`. Only
permissions in the assignable catalog are carried over, so duplicating SuperAdmin does **not**
copy `super_admin`.
