---
tags: [burpsuite, integrations, api]
date: 2024-06-19
---

Faction has a tight integration with [BurpSuite](https://portswigger.net/burp) and you can now find our extension in the [BApp Store](https://portswigger.net/bappstore/f4048e6291214e99a92ca555abee0f74). Here are a few things you can do with the Faction Burp Integration.
1. See your assessment and retest queues.
2. Instant access to your assessment scope and other details.
3. View all findings you and your co-pentesters are reporting.
4. Replay payloads from other pentesters.
5. Add issues in Faction directly from BurpSuite. 

## Install the Burp Faction Integration
You can install the Faction Integration directly from the BApp store. 
1. Open Burp then Click Extensions->BApp Store
3. Search for Faction
4. Click Install

![](/files/Pasted%20image%2020240619150257.png)

## Set Up Faction
In BurpSuite navigate to the Faction tab after you have installed the Faction Integration. From here you need to enter the URL and API key for your user. 

The URL will be your domain plus `api`. Ex `https://faction-test.factionsecurity.com/api`

![](/files/Pasted%20image%2020240619150830.png)

You can retrieve your API Key in Faction by accessing your profile in the upper right corner of the Faction Web Interface. 
![](/files/Pasted%20image%2020240619151123.png)

## Access Your Assessment Queue
Now that Faction is configured you should be able to see you current assessment queue as shown below:

![](/files/Pasted%20image%2020240619151342.png)

Clicking on an assessment will show you the scope, any vulnerabilities that have been reported, and notes that your team has shared with you. 

![](/files/Pasted%20image%2020240619151525.png)

If you select one of the vulnerabilities you can see its full details including screenshots.

![](/files/Pasted%20image%2020240619151631.png)

## Enter Findings into Faction From Burp

Lets say you find an XSS attack and have verified it with BurpSuite. You can add the finding to Faction without ever leaving Burp. Just select the request or response that you want to enter into the report and select "Add New Finding" as shown below:

![](/files/Pasted%20image%2020240619152503.png)

Now you will be presented with the vulnerability findings dialog. Here you can search for an existing vulnerability template to auto populate the details and recommendations. 

Next ensure its being sent to the right assessment. The option will default to the last assessment you selected in the previous section on [Access your Assessment Queue](#access-your-assessment-queue)

Next you have several options. 

- Select the severity or leave the default
- Check or uncheck to include the request and/or response. When checked it will include these options in code blocks in the final report.
- "Snip cookies" when checked will remove all cookies from being added to the report and replace them with `[...snip...]`
- "Extract Selection" when checked will only add the portion of the code you selected in Burp to the report. This is most useful trying to only show the reflected script in the response instead of the full response. 
- Exploit Steps can be included and supports MarkDown Syntax. *Note Screenshots are available though the Burp Extension currently. For this you still need to add them to the Web UI.* 

![](/files/Pasted%20image%2020240619152829.png)

Now you can click **Save** to add it to Faction. All this allows issues to be added seamlessly without breaking your flow. The final result will look something like this.

![](/files/Pasted%20image%2020240619153743.png)


## Replay Findings
The Faction Burp Integration has the ability to replay findings if you included the request in the details. Notice the hyperlink above the request when you select a vulnerability in the Faction BurpSuite Integration. 

![](/files/Pasted%20image%2020240619151840.png)

If you click the hyperlink it will add it to your Burp Repeater. This allows you to replay your own findings and findings from your co-pentesters. The same feature is available for retests!

![](/files/Pasted%20image%2020240619151923.png)

## Add Scan Findings
Anything found in the BurpSuite Scanner can be added directly into Faction using the BurpSuite Integration as well. Just select the issues you want to add and then choose "Send Issues to Faction"

![](/files/Pasted%20image%2020240619154354.png)

Below shows that all issues were combined into two distinct issues.

![](/files/Pasted%20image%2020240619154637.png)

Notice that if you select more than one of the same issue that it will aggregate the URLs into one finding:

![](/files/Pasted%20image%2020240619154521.png)


## Wrapping Up

All of these features have been implemented to make adding issues to pen-testing reports easy and to not break your flow. Nothing worse that being in the zone and then have stop to mess with report formatting or ensuring you capture all the right data in your notes to use later. With Faction you can just add the issues as you find them and move on with your pentest. 



