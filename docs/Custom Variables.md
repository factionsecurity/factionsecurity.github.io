---
tags: [Reporting, Customize]
date: 2024-02-12
---

You can use custom variables to add additional features to Faction. These variables can be used to add additional information to vulnerabilities like a CVSS score or to populate additional data in reports like "product owner", "cost center", etc. 

!!! note
    Faction 1.2 and above has CVSS Scoring built in. You can still use this information as a guide to add your own custom variables. 

## Adding a CVSS Score 
As of Faction version 1.1.25.1, Faction does not have CVSS scores built in but you can add your own easily.  

### Step 1 : Add Custom Fields in Admin
Navigate to Admin -> Settings and add two Custom Fields: **CVSS3.1** and **CVSS String** with variable names `cvss3` and `cvssstring`.

![](files/Pasted%20image%2020240212091803.png)

The **Name** will be what is displayed in the UI and the **variable** name will be used in the report template. We want to apply this to **Vulnerability** so that it will be available when we add vulnerabilities to the assessment.

### Step 2: Update the Report Template

We need to change our report template to include the new variables in the vulnerability section of the template. In this case, we already have a table with vulnerability information and we need to add another row to this table with the new variables. The default template can be downloaded [here](https://github.com/factionsecurity/report_templates/raw/main/default-report-template.docx).

![](files/Pasted%20image%2020240212091208.png)

Notice all custom field variables are pre-populated with `cf`.  If we defined a custom field with a variable of `cvss3` then the reporting variable will be `${cfcvss3}`. 

Note: We needed to change the `loop` variable to inform the Faction reporting engine that the number of rows in the table has changed from 4 to 5. If you are not changing the number of rows then this update is not necessary. 

### Step 3: Add a New Vulnerability to the Assessment

When you add a vulnerability to the assessment the custom fields will be available in the form as shown below:

![](files/Pasted%20image%2020240212092125.png)

Entering the CVSS score will be automatically saved and a report can now be generated with these new Fields. 

![](files/Pasted%20image%2020240212092311.png)








