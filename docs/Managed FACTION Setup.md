---
tags: [Cloud Hosted, Setup]
date: 2023-12-18
---
Below are the Minimal Faction Setup Instructions required to get you all set up and ready to start collaborating on assessments in just a few minutes. With a Faction managed account, we host the servers and maintain the updates for you. Your instance will be hosted in a single-tenant environment to ensure your data is secure. With just a few clicks you will be up and running in minutes. 

## Create Your Managed Account
Every account that gets created will get its own single-tenant instance. To create a new instance go to [https://portal.factionsecurity.com,](https://portal.factionsecurity.com/) Create an Account, and Select a tier that meets your team's needs.

![](/files/Pasted%20image%2020231218081102.png)

This will begin creating your instance of Faction. Wait until the spinner shows a green checkbox before you attempt to access your site. You can then click the URL in the site list to take you to your new Faction Instance.

![](/files/Pasted%20image%2020231218081226.png)

## Create an Admin User
The first time you access Faction you will be presented with a page to create your admin account. Here you need to enter basic information about the user and the option to create a team. **Hacking Team** is the default.

![](/files/Pasted%20image%2020231218081318.png)

## Adding Default Vulnerability Templates

The Faction Default vulnerability database is what makes generating reports quick and painless for pen-testing teams. You can upload your templates or start with an open-source list from [https://github.com/factionsecurity/data](https://github.com/factionsecurity/data)

To add the VulnDB data into Faction just navigate to **Admin**-> **Default Vulnerabilities** and click **Update from VulnDB**. This will import all of their vulnerabilities and set default Categories for the vulnerabilities.

![](files/Pasted%20image%2020231218081440.png)

## Setting Custom Risk Levels (Optional)

By default, Faction adds **Critical**, **High**, **Medium**, **Low**, **Recommended**, and **Informational** risk levels but you have up to 9 that can be set and the defaults can be changed to anything that works for your environment. For instance, **Critical** can be changed to **Priority 1**.

![](files/Pasted%20image%2020231218081517.png)

## Vulnerability Tracking and Remediation SLAs
Different Tiers allow enhanced features within Faction. The **Teams Tier** and above have verification and vulnerability tracking enabled. In **Admin Settings** you can set custom times to alert when the vulnerability needs to be remediated based on its risk setting. For instance, you can set a reminder that a **Critical** vulnerability needs to be remediated 30 days after it's reported and set a past due date of 60 days. This will trigger Faction to alert the correct teams that important issues are close to being past due to ensure issues get closed on time and are never forgotten.

Any values that are missing a date will not be tracked by Faction.

![](files/Pasted%20image%2020231218081607.png)

##  Assessment Checklists

For some assessments, you will want to add checklists to ensure all critical issues are tested. Below is an example of some potential checks that might need to happen on every assessment to ensure applications are tested consistently.

![](files/Pasted%20image%2020231218081706.png)

Once the above is created it will be available in assessments where the assessor can pass/fail the checklist item and even add notes related to why it failed or why it’s not necessary for the application being tested.

![](files/Pasted%20image%2020231218081745.png)

## Additional Configuration Options

The higher-level tiers allow you to configure other options like LDAP and OAuth. You can find additional information below on these settings:

- [Integrate Faction Into OAuth Solutions](/Integrate%20Faction%20into%20OAuth%20Solutions/)
- [Customizing Faction for Self Hosting](/Self-Hosted%20FACTION%20Setup/)
- [Extending Faction](/APIS/App%20Store%20Extension%20API/)
