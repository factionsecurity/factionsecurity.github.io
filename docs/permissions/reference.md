---
description: "Complete reference of every permission in OWASP Faction, grouped by resource, as shown on the Roles admin screen."
---

# Permission reference

Every permission the platform defines, grouped by resource — the same catalog the Roles admin
screen renders as a checkbox matrix.

!!! note "Generated file"
    This page is generated from `backend/src/main/java/com/faction/clientportal/model/Permission.java`
    by `scripts/gen_permission_reference.py`. Edit the enum, then re-run the script; do not edit
    this page by hand.

`super_admin` is not listed here. It is not part of the catalog, is implied by every gate, and
cannot be granted from the Roles screen.


There are **102** permissions across **17** resources.


## Users

| Permission | Description |
| --- | --- |
| `users:read:team` | Read team users |
| `users:edit:team` | Edit team users |
| `users:create:team` | Create team users |
| `users:delete:team` | Delete team users |
| `users:read:all` | Read all users |
| `users:edit:all` | Edit all users |
| `users:create:all` | Create users |
| `users:delete:all` | Delete users |


## Roles

| Permission | Description |
| --- | --- |
| `roles:read:all` | Read all roles |
| `roles:edit:all` | Edit all roles |
| `roles:create:all` | Create roles |
| `roles:delete:all` | Delete roles |


## Organizations

| Permission | Description |
| --- | --- |
| `organizations:read:all` | Read all organizations |
| `organizations:create:all` | Create organizations |
| `organizations:edit:all` | Edit all organizations |
| `organizations:delete:all` | Delete organizations |
| `organizations:read:owned` | Read assigned organizations |
| `organizations:read:org` | Read own organization |


## Applications

| Permission | Description |
| --- | --- |
| `applications:read:all` | Read all applications |
| `applications:create:all` | Create applications |
| `applications:edit:all` | Edit all applications |
| `applications:delete:all` | Delete applications |
| `applications:read:owned` | Read assigned applications |
| `applications:create:owned` | Create owned applications |
| `applications:read:org` | Read organization applications |
| `applications:create:org` | Create organization applications |
| `applications:edit:org` | Edit organization applications |


## Assessments

| Permission | Description |
| --- | --- |
| `assessments:read:team` | Read team assessments |
| `assessments:edit:team` | Edit team assessments |
| `assessments:create:team` | Create team assessments |
| `assessments:delete:team` | Delete team assessments |
| `assessments:read:all` | Read all assessments |
| `assessments:edit:all` | Edit all assessments |
| `assessments:create:all` | Create assessments |
| `assessments:delete:all` | Delete all assessments |
| `assessments:edit:self` | Edit own assessments |
| `assessments:read:assigned` | Read assigned assessments |
| `assessments:edit:assigned` | Edit assigned assessments |
| `assessments:read:owned` | Read assessments of owned applications |
| `assessments:read:org` | Read organization assessments |


## Vulnerabilities

| Permission | Description |
| --- | --- |
| `vulnerabilities:read:assessment` | Read assessment vulnerabilities |
| `vulnerabilities:edit:assessment` | Edit assessment vulnerabilities |
| `vulnerabilities:create:assessment` | Create assessment vulnerabilities |
| `vulnerabilities:delete:assessment` | Delete assessment vulnerabilities |
| `vulnerabilities:read:team` | Read team vulnerabilities |
| `vulnerabilities:edit:team` | Edit team vulnerabilities |
| `vulnerabilities:create:team` | Create team vulnerabilities |
| `vulnerabilities:delete:team` | Delete team vulnerabilities |
| `vulnerabilities:read:all` | Read all vulnerabilities |
| `vulnerabilities:edit:all` | Edit all vulnerabilities |
| `vulnerabilities:create:all` | Create vulnerabilities |
| `vulnerabilities:delete:all` | Delete all vulnerabilities |
| `vulnerabilities:read:org` | Read organization vulnerabilities |
| `vulnerabilities:retest:org` | Request vulnerability retests |
| `vulnerabilities:comment:org` | Comment on organization vulnerabilities |
| `vulnerabilities:read:owned` | Read vulnerabilities of owned applications |
| `vulnerabilities:comment:owned` | Comment on vulnerabilities of owned applications |
| `vulnerabilities:retest:owned` | Schedule retests for owned applications |


## Reporting

| Permission | Description |
| --- | --- |
| `reporting:create` | Create reports |
| `reporting:download` | Download reports |
| `reporting:download:owned` | Download reports for owned applications |


## Report Templates

| Permission | Description |
| --- | --- |
| `report_templates:create:all` | Create report templates |
| `report_templates:read:all` | Read all report templates |
| `report_templates:edit:all` | Edit all report templates |
| `report_templates:delete:all` | Delete report templates |


## Vulnerability Categories

| Permission | Description |
| --- | --- |
| `vulnerability-category:create` | Create vulnerability categories |
| `vulnerability-category:edit` | Edit vulnerability categories |
| `vulnerability-category:delete` | Delete vulnerability categories |


## Default Vulnerabilities

| Permission | Description |
| --- | --- |
| `default-vulnerabilities:create` | Create default vulnerabilities |
| `default-vulnerabilities:edit` | Edit default vulnerabilities |
| `default-vulnerabilities:delete` | Delete default vulnerabilities |


## Checklist Templates

| Permission | Description |
| --- | --- |
| `checklist:create` | Create and manage checklist templates |
| `checklist:edit` | Edit checklist templates |
| `checklist:delete` | Delete checklist templates |


## Survey Templates

| Permission | Description |
| --- | --- |
| `survey:create` | Create and manage survey templates |
| `survey:edit` | Edit survey templates |
| `survey:delete` | Delete survey templates |
| `survey:complete` | Complete assigned surveys |


## System Config

| Permission | Description |
| --- | --- |
| `config:write` | Edit system configuration |
| `sso:config:read` | Read SSO configuration |
| `sso:config:write` | Write SSO configuration |
| `ai:config:read` | Read AI provider configuration |
| `ai:config:write` | Write AI provider configuration |
| `audit:logs:read` | Read audit logs |
| `extensions:read` | Read installed extensions |
| `extensions:write` | Install and configure extensions |


## Peer Review

| Permission | Description |
| --- | --- |
| `peerreview:read:all` | Read all peer reviews |
| `peerreview:read:team` | Read team peer reviews (not yet enforced) |
| `peerreview:edit:all` | Edit all peer reviews |
| `peerreview:edit:team` | Edit team peer reviews (not yet enforced) |
| `peerreview:create:all` | Create peer reviews for any assessment |
| `peerreview:create:assessment` | Create peer reviews for an assessment (not yet enforced) |


## API Keys

| Permission | Description |
| --- | --- |
| `apikeys:create:self` | Create your own API keys |
| `apikeys:read:self` | Read your own API keys |
| `apikeys:delete:self` | Revoke your own API keys |
| `apikeys:read:system` | Read system (service-account) API keys |
| `apikeys:delete:system` | Revoke system (service-account) API keys |


## Campaigns

| Permission | Description |
| --- | --- |
| `campaigns:read:all` | Read all campaigns |
| `campaigns:create:all` | Create campaigns |
| `campaigns:edit:all` | Edit campaigns |
| `campaigns:delete:all` | Delete campaigns |


## Manager Dashboard

| Permission | Description |
| --- | --- |
| `manager_dashboard:read:all` | Read manager dashboard |

