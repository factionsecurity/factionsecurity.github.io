---
tags: [AI, LLM, Enterprise]
date: 2026-04-16
---
![](/files/Pasted%20image%2020260416154601.png)

When a vulnerability is updated or deleted, Faction automatically runs a background review of any incomplete checklist items associated with the assessment. The AI compares each checklist item against the full list of vulnerabilities and marks items as Fail where a matching vulnerability is found.

!!! note
	This feature is only available on Enterprise and having and active AI Configuration. 


- Items are only marked Fail — the AI does not mark items as passed
- Items already manually reviewed (Pass, Fail, or N/A) are not overwritten
- The notes field on each failed item is updated to read: "Updated by Faction AI: matching {Vulnerability Name}"
- Results are logged to the server console for auditability

This feature works with any checklist type, including OWASP Top 10, PTES, and custom checklists. If checklist items have vulnerability mappings configured (e.g. an OWASP item mapped to Injection vulnerabilities), those mappings are included as hints in the AI prompt to improve accuracy.



