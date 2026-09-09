---
description: "Which OWASP Faction permissions are enforced as gates, which narrow the records returned, and where each is checked in the code."
---

# What is enforced

A permission always controls the **gate** — whether the endpoint can be called. It does not
always control the **scope** — which records come back. This page records which is which, so a
role is granted with an accurate picture of what it opens.

## Scoped: the permission narrows what you see

| Permission | Enforced by |
| --- | --- |
| `assessments:read:{all,org,owned,team,assigned}` | `AccessScopeService.resolveAssessmentScope` — SQL filters on the list, `AssessmentScope.permits()` on single records |
| `assessments:edit:{all,team,assigned}` | `resolveAssessmentEditScope`, resolved separately from read |
| `assessments:delete:{all,team}` | `resolveAssessmentDeleteScope`, resolved separately again — a role can delete its team's work while editing only its own |
| `vulnerabilities:read:{all,org,owned,team,assessment}` | `VulnerabilityScopeResolver` — the list, the severity summary, the remediation queue, and single-vulnerability lookups |
| `peerreview:{read,edit}:team` | `PeerReviewService.sharesTeam` — the queue and every single-review action |
| `peerreview:create:assessment` | the service additionally requires the caller to be one of that assessment's assessors |
| `users:{read,edit,create,delete}:team` | `UserService` — the list is filtered to teammates, and create/update force the target into one of your own teams |
| Retest lists | `RetestService.filterToScope` — each row is kept only if `checkAssessmentAccess` allows its assessment |

## Gate-only: the permission opens the door and nothing narrows it

!!! danger "Read this before granting these"
    These behave as system-wide grants regardless of the tier in the name.

- **`assessments:create:team`** — the new assessment's `teamId` comes straight from the request
  and is never checked against the caller's teams. A holder can create an assessment for any
  team, or for none. Three seeded roles carry it — **Pentester**, **Pentester-Team**, and
  **Scheduling-Team** — so a team-scoped scheduler can book work onto another team even though
  every *read* they have is team-bounded. Creating an assessment with no team at all is the more
  common accident: nothing team-scoped can see it afterwards.
- **`vulnerabilities:{edit,create,delete}:*`** — the verb tiers gate the endpoint but do not
  themselves narrow anything. What actually bounds a write is the assessment access check
  (`VulnerabilityService.enforceOrgScope` → `checkAssessmentAccess`), so a caller can modify
  findings on exactly the assessments they can reach — regardless of which tier of the edit
  permission they hold.

## Login-only surfaces that narrow in the service

A few endpoints are gated on being logged in (`@AuthenticatedOnly`) rather than on a permission,
because the callers who need them hold no relevant grant. The narrowing then has to live in the
service, and is worth knowing about:

**`GET /users/mentionable`** — the editor's `@` autocomplete. External (portal) users hold no
`users:read:*` grant at all, but still have to address the people they are working with, so
`MentionableUserService` decides who is addressable:

- **External callers** see their own organization's portal users, plus the remediation contact
  (the vulnerability's `remediationOwnerId`) and whoever is already on the thread (the
  vulnerability's `subscribers`, or the people who have commented on the application). A user
  belonging to a *different* organization is dropped unconditionally, by any route. Staff accounts
  carry no organization, which is exactly what lets the remediation contact through while another
  client's users cannot be.
- **Internal callers** get the directory their `users:read:*` scope already allows, resolved by
  `UserService` — so mentions inherit the team scoping rather than defining a second one.
- The conversation is only consulted after an access check on it, so the subscriber list cannot be
  used to probe threads on someone else's work.
- The response carries a username and display name and nothing else: a mention picker must not
  become a way to read colleagues' emails, roles, or organizations.

## Defaults when nothing matches

The two resolvers fail in opposite directions, which is deliberate but easy to trip over:

- **Assessments** — a caller with no `assessments:read:*` authority resolves to `DENIED` and sees
  nothing. Internal users used to fall through every check and see everything; that is what made
  `:team` and `:assigned` indistinguishable from `:all`.
- **Vulnerabilities** — a caller with no vulnerability read scope is treated as **unrestricted**.
  The endpoint gate is the only thing stopping them, so an endpoint that forgets its
  `@RequiresPermission` leaks the whole vulnerability corpus rather than nothing.

`manager_dashboard:read:all` is intentionally independent of both. It is a deliberate cross-team
view: holding it exposes every assessment and vulnerability *through the dashboard* even with no
`assessments:read:*` grant, and holding `assessments:read:*` does not expose the dashboard.

## Peer review's separate notion of "team"

`PeerReviewService` derives an assessment's teams from its assessors' `teamIds`, while
`AccessScopeService` filters on the assessment's own `teamId` column. They can disagree: an
assessment with no `teamId`, staffed by members of team A, is out of scope for a team-A
pentester's assessment list but in scope for their peer-review queue.

## Verifying a claim on this page

Enforcement is easiest to confirm from the tests, which assert the runtime behavior rather than
the intent:

| Area | Test |
| --- | --- |
| Vulnerability list / summary / single | `GlobalVulnerabilityListTest`, `VulnerabilitySummaryTest` |
| Remediation queue | `RemediationQueueListTest` |
| Retest lists | `RetestTeamScopeTest` |
| User list and single-user reads | `UserTeamScopeTest` |
| Assessment deletion | `AssessmentDeleteScopeTest` |
| Who an external user may @mention | `MentionableUserServiceTest` |
| Seeded roles and their permission sets | `BootstrapServiceTest` |
| Every endpoint makes an explicit authorization decision | `EndpointAuthorizationArchitectureTest` |
