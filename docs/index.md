---
keywords: "pentest reporting tool, penetration testing management software, automate pentest reporting, pentest report generator, AI pentest report writing, open source pentest reporting, self-hosted pentest reporting, vulnerability management, remediation tracking, remediation SLA, application security posture management, OWASP Faction"
description: "OWASP Faction is open source penetration testing management software. Automate pentest reporting from DOCX templates, write findings with AI, collaborate as a team, and track vulnerability remediation with SLAs. Self-hosted, Apache-2.0."
---

![OWASP Faction](files/owasp-faction-logo.png){ .home-logo }

<p class="home-tagline"><strong>Report Less, Break More</strong></p>

<p class="home-badges" markdown>
[![Latest release](https://img.shields.io/github/v/release/factionsecurity/OWASP-Faction-2?style=flat&logo=github&label=Release&color=ab1b93)](https://github.com/factionsecurity/OWASP-Faction-2/releases/latest)
[![YouTube](https://img.shields.io/badge/YouTube-%40factionsecurity-FF0000?style=flat&logo=youtube&logoColor=white)](https://www.youtube.com/@factionsecurity)
[![TikTok](https://img.shields.io/badge/TikTok-%40factionsecurity-000000?style=flat&logo=tiktok&logoColor=white)](https://www.tiktok.com/@factionsecurity)
[![Substack](https://img.shields.io/badge/Substack-%40factionsecurity-FF6719?style=flat&logo=substack&logoColor=white)](https://substack.com/@factionsecurity)
</p>

Penetration test management for teams that produce reports for a living.

Faction runs the whole engagement in one place: scheduling the assessment, recording the findings as you test, getting them peer reviewed, generating the client report, and then tracking every issue through retest and remediation until it is closed. It is self-hosted, open source under Apache-2.0, and yours to change.

## Why teams use it

### Reports write themselves

The report is a DOCX template you design in Word, with variables for everything Faction knows about the assessment. Generate it and every finding, screenshot, severity colour and summary table lands in your layout, as DOCX and PDF. Findings come from a reusable vulnerability library so the common ones are already written, and AI prompts running in your own voice turn a tester's steps to reproduce into a description, a recommendation and an executive summary. See [Reporting](reporting/index.md) and [Templating](templating/index.md).

### Built for teams

Assessments are scheduled against a shared calendar that shows who is free and who is booked. Assessors work on the same assessment at the same time, with edit locks, comments and @mentions on findings. Every report goes through a peer review queue with tracked changes and diffs before it reaches a client, and checklists enforce that nothing was skipped. Dashboards give pentesters, managers and remediation owners each their own view.

### Vulnerabilities are tracked, not just reported

A finding gets a unique tracking ID and keeps it across every assessment it appears in. Retests are scheduled against the original findings, and remediation is tracked stage by stage, with owners, planned dates and SLA clocks that warn and escalate when a fix is late. Exceptions are recorded with approvals and expiry dates, so accepted risk is visible instead of forgotten.

### Extendable

A JAR-based App Store lets you hook your own code into vulnerability, report and assessment events, whether that is pushing findings to a ticketing system, pulling assets from an inventory, or adding a section to the report. Faction 1 extensions load unmodified. There is a full REST API and API keys with scoped permissions for everything else.

### An ASPM foundation

Because every finding carries its application, its asset, its severity, its owner and its remediation history, Faction is a system of record for application security posture, not only a report generator. Managers see open risk by application and organization, remediation owners see what is theirs, and the same finding is never counted twice.

## Faction for

- [Automating pentest reporting](solutions/automate-pentest-reporting.md) from your own Word templates
- [Writing manual pentest reports with AI](solutions/ai-pentest-report-writing.md), in your voice, on your provider
- [Managing large penetration testing teams](solutions/managing-pentest-teams.md) with scheduling, collaboration and peer review
- [Tracking vulnerabilities and remediation SLAs](solutions/vulnerability-management-sla.md) after the report is delivered

## Sections

<div class="grid cards" markdown>

- **[Getting Started](getting-started/index.md)** — schedule a first assessment, add findings
  from the built-in library, and generate and preview the report with the default template.
- **[Reporting](reporting/index.md)** — DOCX report templates and every variable they can use,
  user defined fields, and assessment checklists.
- **[Templating](templating/index.md)** — reusable content templates for the editors, and AI
  prompts that write descriptions, recommendations and executive summaries in your own style.
- **[Solutions](solutions/index.md)** — what Faction is for: automated pentest reporting, AI report
  writing, managing large teams and remediation tracking.
- **[Permissions](permissions/index.md)** — the authorization model: how a permission string is
  built, which scope tiers exist, what each one actually restricts at runtime, and what the
  built-in roles grant.

</div>

## Install it

Docker is the only requirement. One command checks prerequisites, pulls the images and writes a `.env` with generated secrets:

```bash
curl -fsSL https://raw.githubusercontent.com/factionsecurity/OWASP-Faction-2/main/install.sh | bash
cd owasp-faction-2
docker compose up -d
```

Then open `http://localhost:8080`, sign in as `admin` / `admin123`, and change that password before anyone else can reach the install. [Running OWASP Faction](getting-started/install.md) covers the installer's options, installing by hand, upgrading and what the open source edition includes.

## About this site

The site is built with [MkDocs](https://www.mkdocs.org/) and the Material theme, and lives in the
[factionsecurity.github.io](https://github.com/factionsecurity/factionsecurity.github.io) repository.
Pages are Markdown under `docs/`, the navigation is defined in `mkdocs.yml`, and the
[Faction 1.x documentation](/faction1.x/) is a second MkDocs site under `faction1.x/` that is built
alongside this one.

Everything runs through [mise](https://mise.jdx.dev), which creates the Python environment on first use:

```bash
mise run up        # serve both sites with live reload at http://127.0.0.1:8000
mise run up-1x     # serve only the Faction 1.x docs at http://127.0.0.1:8001
mise run build     # build both sites into site/ (this one in strict mode)
mise run deploy    # build both and publish site/ to the gh-pages branch
mise run gen       # regenerate the permission reference from the backend source
mise run check     # fail if generated pages are stale or a build breaks
```

Some pages are generated from the application source rather than written by hand. They say so
at the top and name the script that produces them. Regenerate them with `mise run gen` after
changing the code they describe, rather than editing the page.
