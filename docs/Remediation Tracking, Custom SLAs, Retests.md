---
tags: [Remediation, Retests, Core Features]
date: 2024-03-15
---
FACTION has remediation tracking built in! When you close out an assessment all the vulnerabilities in that assessment start tracking based on your custom SLAs. With the custom SLAs you can set reminders when a vulnerabilities is approaching a due data and another when the it is past due. 

## Setting Custom SLAs
Navigate to Templates -> Default Vulnerabilities. Here you find a table that lets you set your vulnerability tracking times. 
![](files/Pasted%20image%2020240315003554.png)

Each vulnerability severity level will have a Warning date and a Past Due date. These are measured in days after the assessment is completed. *All empty inputs represent Untracked issues.* 

In the above screenshot, Critical vulnerabilities will have a remediation due date that is 60 days and a warning set at 30 days after the assessment is completed.  High vulnerabilities are expected to be remediated in 120 days and have a warning at 60 days after assessment completion. 
Note that all other vulnerabilities are not tracked by FACTION because the inputs are all blank. 

## Remediation Dashboards and Retests

You can see the status of all past and approaching due dates in the Remediation Queue. 
![](files/Pasted%20image%2020240315004352.png)

This dashboard allows assessment teams to easily see all issues that require remediation and the current state of the vulnerability. 

In the above screenshot, there is one issue that is Past Due and several others that are close to being past due. Clicking on the past due issue lets you easily schedule it for retest as shown below:
![](files/Pasted%20image%2020240315005103.png)

## Adding Follow Up Notes
![](files/Pasted%20image%2020240315005359.png)

You can add notes to all tracked vulnerabilities. You can add follow-up notes from the development teams, annotate delays in schedules, or other information you might need later to stay on top of the remediation. 

The Note History stores not only notes but also tracks the passing and failing of retests. 