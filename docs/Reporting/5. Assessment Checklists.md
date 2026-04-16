---
tags: [Reporting, Customize, Variables, Checklists, Assessments, Extensions, App Store]
date: 2025-07-08
---

### Overview 
When conducting frequent penetration tests, having assessment-specific checklists that all assessors follow and document is critical for ensuring consistency, thoroughness, and accountability. These checklists act as structured guides that standardize testing procedures, helping teams avoid oversights and maintain coverage across all critical areas of an environment. Without them, even experienced assessors may miss essential steps due to time constraints, complexity, or assumptions about low-risk areas. A well-maintained checklist also ensures that repeatable methodologies are applied across engagements, making results more reliable and easier to compare over time.

Additionally, documented checklists provide transparency for clients and stakeholders by showing exactly what was tested and how. This supports compliance requirements, helps justify findings, and allows for more meaningful remediation planning. In team environments, it also facilitates knowledge sharing, onboarding of new assessors, and quality assurance reviews. Ultimately, standardized checklists are a foundational practice for delivering high-quality, trustworthy, and defensible penetration testing services.

 Faction includes built-in support for Checklists in both the Open Source and Enterprise versions. You can create and manage as many checklists as needed—such as OWASP Top 10, Mobile Assessment Checks, or Network Assessment Tests. Once added, these checklists can be enforced as part of your assessments and even integrated into Peer Reviews. This provides an excellent way to ensure that assessments remain consistent, thorough, and aligned with best practices.

## Adding a Checklist 
In this example we will an OWASP Top 10 Checklist.

1. Navigate to Admin->Checklists
2. Click **Create new checklist**
3. Start adding items to the checklist. 
4. Ensure you check the Assessment Type at the bottom under **Required For**. This ensures checklists are assessment specific. 
![](/files/Pasted%20image%2020250708014034.png)

## Filling Out Checklists in Assessments
There is a **Checklists** tab in *Assessments*. The assessor will need to add checklists that are required for this assessment type. ***The assessment cannot be finalized until all checklist items are validated. ***
![](/files/Pasted%20image%2020250708014420.png)

## Adding Checklists to Reports (Optional)
In addition to making it a sanity check for your assessments you can choose to add certain checklist to your generated reports using one of our App Store Extensions. 

### Enable the CheckList Extension
Follow these steps to add a checklist to your assessment. 

1. Download the [CheckList Extension here](https://github.com/factionsecurity/checklist-report-extension/releases)
2. Navigate to Admin->AppStore
3. Click **Install Extension** from the upper right
4. Upload faction-report-checklist-X.X.jar
5. Click Install
6. Back on the Installed Extensions table switch the extension to **On**
	![](/files/Pasted%20image%2020250708012904.png)

### Update The Report Template
Checklists can be added anywhere to your report using variable names. The variable name is based on the title of your checklist. For instance if you created a checklist named ***OWASP TOP 10***, then the variable name will be `${checklist-owasp-top-10}`.

![](/files/Pasted%20image%2020250708015655.png)

Once the report template is updated, the report can be generated from the **Finalize** tab in the assessment. The default result will look like the following:

![](/files/Pasted%20image%2020250708015518.png)

### Customizing the CheckList Extension Output
The Checklist Extension has several configureable options. You can change text thats printed on Pass, Fail, or N/A status. You can also change the background and foreground colors. 

To configure the extension, navigate to Admin->App Store and select the Checklist Extension. There are options at the bottom of the screen. 

![](/files/Pasted%20image%2020250708020140.png)







