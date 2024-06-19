---
tags: [App Store]
date: 2024-03-25
---
✨ We are excited to release the first iteration of the Faction App Store! ✨

The App Store is where developers can build custom integrations with Faction. These can be anything from sending vulnerabilities to external bug trackers to adding custom graphics to your automated pentest reports! 
<!-- more -->
We want to make this process really easy and took inspiration from [Burp Suite](https://portswigger.net/burp/documentation/desktop/extensions/creating) on the design. If you have ever made an extension for Burp then you should be able to get up and running pretty quickly. 

### What Can Be Extended?
With this initial release, you can extend Faction by:

- Including your own application inventory database to the application search features and populate results in Faction like the Application ID, Distribution Lists, and Application Name. 
- Triggers when an assessment state changes (created, updated, or finalized). You can use this to send emails to a distribution list that an assessment has been scheduled for certain dates. When the assessment is finalized you can choose to send only the vulnerabilities of a certain criticality to an external tracking system as well as send to different tracking systems depending on the type of assessment. 
- Triggers when a vulnerability state is changed. When a tracked vulnerability is retested and pass/fail, you can create a custom workflow and alert key stakeholders that the issue succeeded or failed. 
- Update reports when they are generated. You can use this to add custom variables to your reporting templates and replace the contents with data from an external system or add custom charts and graphics to give your reports a more polished look. 

The full documentation on the API can be found [here](/APIS/App%20Store%20Extension%20API)

### Custom Settings
Extensions are built so that you can add your own configuration options that can be stored in the Faction Database. Things like a user-editable hostname or API key can be configured in your extension. Based on how you set up your configuration you can make data like passwords and API keys hidden in the UI and encrypted at rest. 

![](/files/Pasted%20image%2020240325105733.png)

### Extension Chain
Extensions can be chained in any order. Once you add apps and enable them in Faction, the UI allows you to drag the extension to anywhere in the list. This allows you to create one extension that processes data and returns a result that can be processed by the next extension. 

| Before Order Change | After Order Change |
| --- | --- |
| ![](/files/Pasted%20image%2020240325105756.png) | ![](/files/Pasted%20image%2020240325105827.png) |


You can use this to create one extension that returns a JIRA Tracking number for all vulnerabilities in the finalized assessment, they take those numbers and process them into another system and on and on down the chain. 


### Example Extensions
You can review the source code for our initial apps [here](/Faction%20App%20Store%20Extensions). This list will grow over time but currently, there are 2 (JIRA Integration, Vulnerability Bar Charts). 

### Submit Your Own
We can't think of everything! We encourage developers to submit their own extensions and we will add them to our list of Approved Extensions. Send an email to develop [ at ] factionsecurity [dot] com with a link to your GitHub and a brief explanation of what it does. 

### Conclusion
We hope you enjoy the new  App Store and other new features that are part of this 1.2 Release. Faction is open-source and free to use. Please leave us feedback in either our GitHub [Discussion Boards](https://github.com/orgs/factionsecurity/discussions) or by [submitting Issues](https://github.com/factionsecurity/faction/issues). 

If you want to help support the project and ensure its longevity then consider being a sponsor... It's good karma!  ❤️

__Sponsor Options__

- [GitHub Sponsor](https://github.com/sponsors/factionsecurity)
- [Patreon](https://www.patreon.com/null0perat0r)
- [Open Collective](https://opencollective.com/faction)
