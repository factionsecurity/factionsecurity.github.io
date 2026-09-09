---
description: "How authorization works in OWASP Faction: permission gates on every endpoint and scope tiers that restrict which assessments and findings a role can see."
---

# Permissions overview

Authorization has two independent layers. Both must pass, and confusing them is the source of
most "why can this role see that?" questions:

1. **The gate** — may this caller call this endpoint at all? Enforced by `@RequiresPermission`
   on the controller method.
2. **The scope** — of the records the endpoint could return, which ones may *this* caller see?
   Enforced inside the service or query layer.

A permission string grants the first. It does **not** automatically grant the second: several
permissions open a door without narrowing what is behind it. Which ones is documented in
[What is enforced](enforcement.md).

## Anatomy of a permission

```
assessments : read : team
└─ resource   └─ action  └─ scope
```

- **resource** — what is being acted on (`assessments`, `vulnerabilities`, `users`, …). Groups
  the permission in the Roles screen.
- **action** — the verb: `read`, `edit`, `create`, `delete`, plus a few resource-specific ones
  (`download`, `comment`, `retest`, `complete`, `write`).
- **scope** — how wide the reach is: `all`, `org`, `team`, `owned`, `assigned`, `assessment`,
  `self`, `system`. See [Scopes](scopes.md).

Not every permission has all three segments. `reporting:create` and `survey:complete` are
unscoped, and a few carry a compound resource: `sso:config:read` is the *SSO config* resource
with a `read` action and no scope — **not** the `sso` resource scoped to `read`. When parsing a
permission string, read it from the right and treat a trailing segment as a scope only when it
is one of the known tiers.

## How gates are enforced

```java
@RequiresPermission({Permission.ASSESSMENTS_READ_ALL,
                     Permission.ASSESSMENTS_READ_TEAM,
                     Permission.ASSESSMENTS_READ_ASSIGNED})
```

- **Any-of.** The caller needs *one* of the listed permissions, not all of them.
- **Exact string match.** There is no hierarchy and no wildcard: `assessments:read:all` does not
  imply `assessments:read:team`. An endpoint that lists only the `:all` variant is unreachable
  for a `:team` role, however sensible the tier looks. This is why the gates enumerate every
  tier they mean to accept.
- **`super_admin` is implied everywhere.** It is checked before the annotation's list, so
  endpoints never list it — and must not.
- Coverage is enforced by a test: `EndpointAuthorizationArchitectureTest` fails the build for
  any endpoint with neither `@RequiresPermission` nor `@AuthenticatedOnly`.

## Where the catalog comes from

`Permission.java` is the single source of truth. `GET /api/v1/permissions` serves it grouped by
resource, and the Roles admin screen renders that response as a matrix of scope rows against
action columns. Adding an enum constant makes the permission assignable with no UI change.

Two consequences worth knowing:

- `super_admin` is **not** in the catalog, so it has no checkbox and cannot be granted through
  the Roles screen. Duplicating a role in the UI copies only catalog permissions for the same
  reason.
- A permission string stored on a role that no longer exists in the enum is dropped on startup
  by `BootstrapService.migrateRolePermissions()`, which also applies historical renames. A typo
  in a permission grants nothing rather than failing loudly, so grant from the UI, not by
  hand-editing role documents.

## Roles

A role is a name plus a list of permission strings. Users hold roles; the authorities on their
token are the union of every role's permissions. Roles marked **external** are the ones
assignable to portal (client) users, and should hold only `:org` or `:owned` scoped permissions.

See [Built-in roles](roles.md) for what ships out of the box.
