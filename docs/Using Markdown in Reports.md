---
tags: [Markdown, Reporting, Core Features, Burp Suite]
date: 2024-03-17
---
When exploiting a vulnerability in a penetration test it is important to capture your attack steps quickly and thoroughly so you don't have to spend extra time remembering and re-validating what you did when it's time to report on the finding. Nothing can break your flow more than having to stop what you are doing to format text, fix hyperlinks or build numbered lists of steps. Markdown is one of the quickest ways to type formatted text and capture these details effortlessly. 

!!! note "Pro Tip!"

    The API fully supports Markdown. This makes it easy to develop automated tools that can add issues or other text to Faction with formatted text via the API. 


Here are some examples of how you can use markdown in Faction.

## Exploit Steps
You can enter Markdown directly into the details editor when adding a new vulnerability. Once you enter the text, highlight just the part you want to convert to markdown and click the Markdown button in the toolbar. 

![](/files/Pasted%20image%2020240317122727.png)

After you select the Markdown button your text will be converted to rich text as shown below:
![](/files/Pasted%20image%2020240317122948.png)

You can also perform this in a code block if you want to write your Markdown in a monospaced font.  First, select `Code` as shown below:
![](/files/Pasted%20image%2020240317123222.png)

Then start entering your text in the code block as shown here.
![](/files/Pasted%20image%2020240317123535.png)

Select the text in the code block and click the Markdown button
![](/files/Pasted%20image%2020240317124431.png)

## Faction Burp Suite Extension
If you find a vulnerability while using the Faction Burp extension, you can add the finding and all details directly through the extension. Below is an example of cross-site scripting:
![](/files/Pasted%20image%2020240317125704.png)

In Burp Suite, select the request and select Add New Finding:
![](/files/Pasted%20image%2020240317125749.png)

A dialog box will open that lets you search for the vulnerability type (in this case Cross Site Scripting) and allow you to enter your details on how to recreate the exploit. 

![](/files/Pasted%20image%2020240317130047.png)

Now if we navigate back into Faction and view the details we will see the exploit steps displayed in rich text. 

![](/files/Pasted%20image%2020240317130408.png)

## Executive Summaries  and Scoping
You can use Markdown in your Executive Summaries as well to quickly type up your high level assessments of the application and provide guidance on how to prioritize the findings.   
![](/files/Pasted%20image%2020240317124018.png)

Select the text and click Markdown to convert!
![](/files/Pasted%20image%2020240317124033.png)

You can also add scoping information in tables without messing with table editors and setting hyperlinks which can be a pain sometimes. 
![](/files/Pasted%20image%2020240317124827.png)

![](/files/Pasted%20image%2020240317124858.png)



