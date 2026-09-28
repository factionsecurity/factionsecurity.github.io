---
keywords: "bulk create assessments, CSV import, bulk schedule pentests, assessment upload, Faction 1.x migration"
description: "Bulk-schedule assessments in OWASP Faction by importing a CSV: the column format, how applications and campaigns are auto-created, the preview step, and mapping from the Faction 1.x upload format."
---

# Bulk-import assessments from a CSV

If you need to schedule many assessments at once, for example when standing up a new
organization or bringing over a backlog of engagements, you can import them from a CSV
instead of creating them one at a time.

## Where to find it

On the **Scheduling** page, click **Import CSV** next to **Create Assessment**.

!!! info "Who can see this"
    The **Import CSV** button only appears for users with the `assessments:create:all`
    permission (super admins always have it). See [Permission reference](../permissions/reference.md).

## The CSV format

Click **Download Template** in the import dialog for a starter file with the correct headers,
including one column for every assessment-level custom field defined on your report templates,
and an example row.

Column headers are matched **ignoring case**, and column order does not matter. Each column
can appear only once.

!!! note "Size limits"
    A file can hold up to **2,000 assessments** (rows after the header) and be up to **10 MB**.
    Split anything bigger into several files and import them one after another.

| Column | Required | Meaning |
|---|---|---|
| `name` | Yes | The assessment name (255 characters or fewer) |
| `appId` | One of `appId` or `applicationName` | Looks up the application by its app ID. If nothing matches, a new application is created |
| `applicationName` | | Looks up the application by name when `appId` is blank. Also the name used for a newly created application |
| `assessmentType` | Yes | The assessment type name. It must already exist |
| `startDate` | Yes | `YYYY-MM-DD` |
| `endDate` | One of `endDate` or `durationDays` | `YYYY-MM-DD`. Cannot be before `startDate` |
| `durationDays` | | A whole number of days, from 0 to 3650, added to `startDate` to get the end date. If both `endDate` and `durationDays` are given, `endDate` wins |
| `assessors` | | Usernames or emails, separated by `;`. Assessors must be internal users, as on the **Create Assessment** form |
| `campaign` | | Campaign name. Unknown names are created if you're allowed to create campaigns; leave it blank to use the default campaign |
| `team` | | Team name. It must already exist |
| `engagementManager` | | Username or email |
| `remediationManager` | | Username or email |
| `reportTemplate` | | Report template name. It must already exist, be active, not deleted, and belong to the row's assessment type. Leave it blank to use the type's default template. If the type has several templates and none of them is the default, name one here |
| `scope` | | Plain text. It is stored as scope's rich text, so line breaks are kept |
| *any other column* | | Treated as an assessment-level custom field, matched by variable name (see below) |

Any column header that is not one of the built-in names above and does not match an
assessment-level custom field's variable name fails the whole file with an "unknown column"
error before anything is previewed.

!!! note "Only assessment-level custom fields"
    The import only recognizes custom fields scoped to the assessment itself. Custom fields
    scoped to vulnerabilities, applications or organizations aren't part of the template and
    can't be set through this import.

## Matching rules

- Every lookup, applications, assessment types, campaigns, teams, report templates, usernames
  and emails, ignores case.
- If a value matches more than one record (for example two report templates whose names differ
  only in case), that row gets an **"Ambiguous"** error instead of Faction guessing which one
  you meant.
- An entry in `assessors`, `engagementManager` or `remediationManager` that contains an `@` is
  looked up by email; otherwise it is looked up by username.

## What gets created automatically

- **Applications** — an unknown `appId` or `applicationName` becomes a new application.
  Several rows with the same new `appId` create it only once, and so do several name-only rows
  (no `appId`) with the same `applicationName`, compared case-insensitively. A row that gives
  an `appId` and a row that gives only the name are treated as two different applications,
  even if the names match, so use `appId` on every row for the same new application.
- **Campaigns** — an unknown `campaign` value becomes a new campaign. Several rows naming the
  same new campaign create it only once. Creating a campaign needs the `campaigns:create:all`
  permission, the same as on the **Campaigns** page. Without it, a row naming a campaign that
  doesn't exist gets a row error, so ask an admin to create the campaign first.

Everything else, assessment types, teams, users and report templates, must already exist in
Faction. Rows that reference something that doesn't exist get a row error rather than having
it created for them.

## Custom fields

Custom fields live on report templates, so a custom-field column is checked against the report
template that row resolves to: the one named in `reportTemplate`, or the assessment type's
default. A value in a custom-field column for a field that isn't on that template is a row
error, and values go through the same validation as the create form (dropdown options, length
limits, and so on). If the assessment type has no report template yet, any custom-field value
in that row is also a row error.

!!! note "Required custom fields aren't enforced here"
    Just like the **Create Assessment** form, required custom fields are not checked at import
    time. They can be filled in on the assessment afterward.

A custom field whose variable name happens to match a built-in column name (for example a field
literally named `team`) can only be set through that built-in column, not as a separate
custom-field column.

## Preview, then create

Choosing a file doesn't import anything by itself. Click **Preview** first to see a row-by-row
breakdown: which application, type, dates, assessors and campaign each row resolves to, whether
it will create a new application or campaign, and any errors.

!!! warning "Nothing is created while any row has an error"
    The **Create N assessments** button stays disabled until every row in the file is error-free.
    Fix the file and preview it again rather than trying to import the valid rows and skip the
    rest.

Once the preview is all clear, check or leave unchecked **Notify stakeholders**, "Send the
assessment-created notifications and emails to assessors, managers and stakeholders". It is
**off by default**, so a large bulk import doesn't flood everyone's inbox; turn it on if you do
want the normal creation notifications and emails to go out for each imported assessment.

Click **Create N assessments**. If nothing has changed since the preview, every row is created
in a single batch. If something changed in the meantime (someone else deleted a template you
referenced, say), the import stops, nothing is created, and you're shown a fresh preview with
the new errors.

## Coming from Faction 1.x

Faction 1.x's assessment upload read its columns by position: the file had a header row, but
1.x skipped it without reading it. Faction 2 matches columns by their header names instead, so
a 1.x file needs to be converted, not just re-uploaded. The columns map as follows:

| Faction 1.x column | Faction 2 column | Notes |
|---|---|---|
| AppID | `appId` | Same lookup by app ID |
| AppName | `applicationName` **and** `name` | Faction 2 needs a `name` column for the assessment name. In 1.x the assessment was named after the application, so copy AppName into both columns |
| Start Date (`YYYYMMDD`) | `startDate` (`YYYY-MM-DD`) | Reformat the date |
| Duration | `durationDays` | |
| Assessment Type | `assessmentType` | 1.x created a missing assessment type for you. Faction 2 doesn't, so create every type before you import |
| Assessors (`"First Last"`) | `assessors` | Faction 2 matches people by username or email, not by display name; list them `;`-separated. They must be internal users |
| Campaign Name | `campaign` | |
| Custom fields (single-quoted JSON) | One column per variable | Each custom field becomes its own column, named by its variable name, instead of a JSON blob |

Faction 1.x's upload also had no preview step and applied each row immediately, with its own
per-row errors. Faction 2 always previews first and only creates the batch once every row is
error-free.
