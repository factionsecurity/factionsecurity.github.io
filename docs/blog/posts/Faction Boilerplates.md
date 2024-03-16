---
tags: 
 - core features
 - boilerplate
 - templating
authors: [null0perat0r]
date: 2024-03-16
---

If you have been doing penetration testing for any length of time you probably have a personal database of vulnerability descriptions, recommendations as well as other text snippets you will inject into various places of your reports. What if, Instead of keeping these in separate files on various computers, what if they were all included in your reporting software?!@! 🤯

Faction IS your database for global boilerplate, default vulnerability templates, personal flare, and just about anything else you can image (well...sorta 🤔). Let's walk through how this is done.
<!-- more -->
## Vulnerability Templates
Let's start with the obvious.... Faction includes over 75 default vulnerability templates when you start. These vulnerability templates include both descriptions and recommendations and are fully customizable by you. You can start with our templates or upload your own as described [here](/Importing%20Your%20Vulnerability%20Templates%20Via%20the%20API/).

When writing your report, type the name of the vulnerability and it will auto-populate in the UI as shown below:
![](/files/Pasted%20image%2020240316111751.png)

Once selected your report will automatically include the severity of the finding, the description, and the recommendation! 💥 Something that would have taken you 30 min to an hour is complete in just a few seconds.
![](/files/Pasted%20image%2020240316112114.png)

These are fully editable in the Default Vulnerabilities section. You can add new ones, update the pre-packaged ones, or delete them all and upload all your own with the [Faction API](/Importing%20Your%20Vulnerability%20Templates%20Via%20the%20API/).

## Assessment Templates
Faction has the option of creating global and personal boilerplates that you can easily add to your reports. Global templates are shared with everyone while personal templates are only available to you. 

### Global Assessment Templates
In Faction, Navigate to Templates -> Assessment Templates. Here you have the option to create text that will be available to all assessors in the platform. This is useful for creating things like Different High-Level Summaries for different report types or adding common risk summaries. 

![](/files/Pasted%20image%2020240316113341.png)

Notice you can include most [faction variables](/Custom%20Security%20Report%20Templates/) in your templates and they will be auto-populated in the generated report. 

As the security assessor, you can easily add these to different sections of your report. Below is a screen-share of using Global Templates in your reports. 

<iframe width="1280" height="641" src="https://www.youtube.com/embed/uucCzTkTfCk?hd=1" title="Using Global Templates in PenTesting Reprots" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### User Assessment Templates
User Assessment Templates work the same as the Global Assessment Templates but are specific to your user account. This can allow you to add your own flare to a report that you might not want to share with the rest of the team. 

To add a User Template just start typing into any of Faction's text editors and then click the Save button in the Template section. Note that User Templates have a different icon beside them in the Template List. 

Below is a walk though of how you would add User templates to save and later recall user-defined boilerplate text.  

<iframe width="1280" height="641" src="https://www.youtube.com/embed/pMrvDNscN80?hd=1" title="Using User Defined Templates in PenTesting Reports" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>