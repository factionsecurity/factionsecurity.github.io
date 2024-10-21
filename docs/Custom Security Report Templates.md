---
date: 2023-12-17
tags: [Reporting, Customize, Variables]
---
![](files/Pasted%20image%2020231217155942.png)

The Faction Report Designer allows you to create custom security report templates for each assessment type. When building reports you need to use the variables listed below. Entering these into your DOCX reports will auto-replace the assessment and vulnerability text when the report is generated. You can even use the same variables in many of the assessor input fields outside of the report template (like Risk Assessment Summaries) and it will auto-populate the fields when the report is generated.

You can download the sample templates here:
 [Sample Templates](https://github.com/factionsecurity/report_templates) 
 
!! note
	You should disable spellcheck in your template document while adding variables. The spellcheck can cause the variables to contain attributes that will make the variable unrecognizable to the Faction document parser. 

 
## GENERAL VARIABLES:

All of these variables can be used anywhere in the DOCX template. Those with a star ⭐️ can be used in the web interface to assist in creating common reusable templates.

- **${TOC}** – Placeholder for the Table of Contents
- **${summary1}** – The high level summary
- **${summary2}** – The objective and scope
- **${asmtId}** – Internal Database ID ⭐️
- **${asmtAppid}** – The assigned Application ID ⭐️
- **${asmtName}** – The Assessment Name ⭐️
- **${asmtAssessor}** – The first assessor assigned to the assessment ⭐️
- **${asmtAssessor_Email}** – The first assessor email address ⭐️
- **${asmtAssessors_Lines}** – All Assessors split into lines ⭐️
- **${asmtAssessors_Comma}** – All Assessors split into a comma delimited list ⭐️
- **${asmtAssessor_Bullets}** – All Assessors split into a bulleted list ⭐️
- **${remediation}** – The Remediation Person assigned to the assessment ⭐️
- **${riskCount*}** – The number of findings at the RiskLevel 0-9 ⭐️
- **${riskTotal}** – The total number of findings at all RiskLevels ⭐️
- **${asmtTeam}** – The Assessor Team Name ⭐️
- **${asmtType}** – The Type of the Assessment ⭐️
- **${asmtStart}** – The Start date of the assessment ⭐️
- **${asmtEnd}** – The End date of the assessment ⭐️
- **${asmtAccessKey}** – Guid to access the client retest queue. ⭐️
- **${today}** – Day the report is generated ⭐️
- **${cfXXXXXX}** – Custom Fields are ones you specify in the admin interface. These are all prefixed with “cf” ⭐️
- **${totalOpenVulns}** - Can be used in retest reports to show a count of open vulnerabilities.  (Since 1.3)
- **${totalClosedVulns}** - Can be used in retest reports to show the total count of closed vulnerabilities. (Since 1.3)

## VULNERABILITY TABLES VARIABLES:

These are only available inside tables.

- **${vulnTable}** – This defines a table to be a vulnerability listing table.
- **${vulnTable Section_Name}** – This defines a table to be a vulnerability listing table for a section of vulnerabilities. See [Reporting Sections](https://docs.factionsecurity.com/Custom%20Security%20Report%20Templates/#Reporting-Sections-(Enterprise/Paid-Feature))(Paid Only Feature).
- **${vulnName}** – The Vulnerability name
- **${rec}** – Vulnerability Recommendation
- **${desc}** – Vulnerability Description
- **${category}** – Category of the vulnerability
- **${severity}** – Severity of each vulnerability.
- **${likelihood}** – Likelihood of the vulnerability
- **${impact}** – Impact of the vulnerability
- **${cvssScore}** – CVSS score of the vulnerability (Since v1.2)
- **${cvssString}** – CVSS vector of the vulnerability (Since v1.2)
- **${count}** – Row Count of the vulnerability
- **${tracking}** – Tracking number of the vulnerability
- **${vid}** – Vulnerability internal database id
- **${openedAt}** - The date the vulnerability began tracking (Since 1.3)
- **${closedAt}** - The date the vulnerability was closed (no longer tracked) (Since 1.3)
- **${remediationStatus}** - Displays only "Open" or "Closed" (Since 1.3)
- **${cfXXXXXX}** – Custom Fields are ones you specify in the admin interface. These are all prefixed with “cf”
- **${color  key=value,key=value}** – The color of the text is based on key-value pairs. [See below for how to set up colors.](https://docs.factionsecurity.com/Custom%20Security%20Report%20Templates/#setting-severity-colors)
- **${cells key=value,key=value}** – The color of the table cell is based on key-value pairs.  [See below for how to set up colors.](https://docs.factionsecurity.com/Custom%20Security%20Report%20Templates/#setting-severity-colors)
- **${loop}** – This variable tells the report generator which row will be repeated.
- **${loop-*}** – This allows multiple rows to be repeated. Example ${loop-1} will repeat the row but the one below it.
- **${details}** – This will insert screenshots and exploit steps for each vulnerability.
- **${noIssuesText}** - This is the default text displayed in the section if no vulnerabilities are reported. (Since 1.3.28)
  
### Example Table Summary Table

|   |   |   |   |
|---|---|---|---|
|${vulnTable}|${color Critical=C00000,High=FFC000}|||
|ID|Finding Name|Impact|Severity|
|${loop}|${count}. ${vulnName}|${impact}|${severity}|

### Example Table Detail Table

|   |   |   |   |
|---|---|---|---|
|${vulnTable}|   |${cells Critical=8064a2,High=c0504d,Medium=e68e00, Low=33D7FF,Recommended=081417,Informational=657376}|   |
|${loop-5}|## 1  ${vulnName}|   |${severity}|
|CVSS:|   |${cvssString}|${cvssScore}|
|Category:|   |${category}|   |
|Description:<br><br>${desc}|   |   |   |
|Recommendation:<br><br>${rec}|   |   |   |
|${details}|   |   |   |

![](files/Pasted%20image%2020240227161500.png)

**Why is the heading yellow?!?! Check [here](/Custom%20Security%20Report%20Templates/#setting-severity-colors)



## VULNERABILITY BLOCK VARIABLES:  
**For when you do not want to use tables to display your vulnerability information. You can use the following variables for inserting vulnerability information outside of a table**

- **${fiBegin} / ${fiEnd}** – Block to repeat against all findings.
- **${fiBegin Section_Name} / ${fiEnd Section_Name}** – Block to repeat a section of findings. See  [Reporting Sections](https://docs.factionsecurity.com/Custom%20Security%20Report%20Templates/#Reporting-Sections-(Enterprise/Paid-Feature)) (Paid Only Feature)
- **${vulnName}** – The Vulnerability name
- **${rec}** – Vulnerability Recommendation
- **${desc}** – Vulnerability Description
- **${category}** – Category of the vulnerability
- **${severity}** – Severity of each vulnerability.
- **${likelihood}** – Likelihood of the vulnerability
- **${impact}** – Impact of the vulnerability
- **${cvssScore}** – CVSS score of the vulnerability (Since 1.2)
- **${cvssString}** – CVSS vector of the vulnerability (Since 1.2)
- **${count}** – Row Count of the vulnerability
- **${tracking}** – Tracking number of the vulnerability
- **${vid}** – Vulnerability internal database id
- **${openedAt}** - The date the vulnerability began tracking (Since 1.3)
- **${closedAt}** - The date the vulnerability was closed (no longer tracked) (Since 1.3)
- **${remediationStatus}** - Displays only "Open" or "Closed" (Since 1.3)
- **${cfXXXXXX}** – Custom Fields are ones you specify in the admin interface. These are all prefixed with “cf”
- **${details}** – This will insert screenshots and exploit steps for each vulnerability.
- **${color  key=value,key=value}** – The color of the text is based on key-value pairs. [See below for how to set up colors.](https://docs.factionsecurity.com/Custom%20Security%20Report%20Templates/#setting-severity-colors)
- **${fill key=value,key=value}** – The color of the background elements is based on key-value pairs.  [See below for how to set up colors.](https://docs.factionsecurity.com/Custom%20Security%20Report%20Templates/#setting-severity-colors)
- **${noIssuesText}** - This is the default text displayed in the section if no vulnerabilities are reported. (Since 1.3.28) 

### Example Block Findings

![](files/Pasted%20image%2020240227160631.png)

**Why is the heading yellow?!?! Check [here](/Custom%20Security%20Report%20Templates/#setting-severity-colors)

## Reporting Sections (Enterprise/Paid Feature)
You can put findings into different sections of your report for paid versions and certain sponsored tiers of Faction. You may want to use sections if you are doing different types of pen tests in one report and need to keep these sections separated. For example, you can segregate findings into  Application Security and Network Security Sections. 

To use sections you need to create the section names in the Faction Report Designer:
![](/files/Pasted%20image%2020241020214807.png)

Once the sections are created in the UI, you can add them to the report in two ways. 
1. Vulnerability Block Variables: `${fiBegin Your_Section_Name}`/`${fiEnd Your_Section_Name}
2. Vulnerability Table Variables: `${vulnTable Your_Section_Name}`

Below is an example of how the template variables work:

![](/files/Pasted%20image%2020241020215154.png)

## CSS FORMATTING:

All of the text generated from Faction is HTML. You can control how it is rendered in the DOCX format using the CSS editor in the Report Designer. You will need to set the CSS to match your report templates. Things like font and size will need to match. Images will need to be forced to resize to the correct dimensions to fit in your reports.

![](files/Pasted image 20231217160124.png)

## SETTING SEVERITY COLORS:

When building reports you most likely will set the text or cell to the color that matches the severity of the finding. To achieve this in FACTION you need to set a default color in the docx template that matches the severity category (i.e. Overall, Likelihood, and Impact). These default colors are in the table below:

|   |   |
|---|---|
|**Category**|**Color Hex**|
|Overall Severity|#FAC701|
|Likelihood|#FAC702|
|Impact|#FAC703|

For Example, a table in MS Word below has pre-filled the color codes for each severity name and category.

![](files/Pasted image 20231217160231.png)

Right-click the overall severity variable, **${severity}**; you can see the default hex code for this color is #FAC701. Likelihood would be set to #FAC02, and Impact would be set to #FAC703.

![](files/Pasted image 20231217160250.png)

Setting the background color for cells works in much the same way. Notice we use the ${cells} variable instead.

![](files/Pasted image 20231217160305.png)

Right-click on the cell and set the color you may only want to use the Overall severity option but you can have multiple cells with each category if you wish.

![](files/Pasted image 20231217160321.png)

Below is an example of the generated report table with colors replaced.

![](files/Pasted image 20231217160335.png)
