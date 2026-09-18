---
description: "Pentest reporting in OWASP Faction: DOCX report templates and every variable they support, user defined fields for findings and assessments, and assessment checklists printed in the report."
---

# Reporting

Faction generates assessment reports from DOCX templates that you design. A template is an ordinary Word document with `${variable}` placeholders; when a report is generated, Faction fills in the assessment details, repeats a block or table row for every finding, applies severity colours, and writes out a finished document.

<div class="grid cards" markdown>

- **[Using DOCX Report Templates](docx-templates.md)** — every variable a template can use, how to lay out findings as a table or as a repeating block, report sections, page breaks, severity colours and CSS formatting.
- **[Code Block Themes](code-block-themes.md)** — copy-and-paste CSS that recolours code blocks in the report: Dracula, Solarized, Nord, Monokai, Gruvbox, GitHub and more, plus how to build your own.
- **[User Defined Fields](user-defined-fields.md)** — add your own fields to findings and assessments, such as an affected URL or an executive summary, and print them in the report.
- **[Assessment Checklists](checklists.md)** — enforce a standard checklist per assessment type, block finalization until it is complete, and print the results in the report.

</div>

## Where things live in Faction 2

| Task | Location |
|---|---|
| Upload a DOCX template, set the report font and CSS, define report sections and custom variables | **Admin → Content & Reporting → Report Designer** |
| Create checklist templates | **Admin → System → Assessment Config → Checklist Templates** |
| Install and enable report extensions | **Admin → System → App Store** |
| Generate the report for an assessment | The assessment's **Finalize** tab → **Report Documents → Generate Report** |

!!! tip "Coming from Faction 1?"
    Templates written for Faction 1 work unchanged in Faction 2, including report sections. The differences are listed at the top of [Using DOCX Report Templates](docx-templates.md#whats-new-in-faction-2).
