---
tags: [Markdown, Reporting, Core Features, Burp Suite]
date: 2024-03-17
---
When exploiting a vulnerability in a penetration test it is important to capture your attack steps quickly and thoroughly so you don't have to spend extra time remembering and re-validating what you did when it's time to report on the finding. Nothing can break your flow more than having to stop what you are doing to format text, fix hyperlinks, or build numbered lists of steps. Markdown is one of the quickest ways to type formatted text and capture these details effortlessly. 

!!! note "Pro Tip!"

    The API fully supports Markdown. This makes it easy to develop automated tools that can add issues or other text to Faction with formatted text via the API. 


Faction supports markdown by default in all editors. Here are some examples of how you can use markdown:

## Exploit Steps
Entering exploit steps is easier with markdown. You can enter the following text and it will automatically show you the formated view on the right. 
```
__Steps to Reproduce__:
1. Go to the home page.
2. Click Login.
3. Enter `<script>alert(123);</script>` in the username parameter. 
```

![](/files/Pasted%20image%2020241020220256.png)


## Faction Burp Suite Extension
If you find a vulnerability while using the Faction Burp extension, you can add the finding and all details directly through the extension. Below is an example of cross-site scripting:
![](/files/Pasted%20image%2020240317125704.png)

In Burp Suite, select the request and select Add New Finding:
![](/files/Pasted%20image%2020240317125749.png)

A dialog box will open that lets you search for the vulnerability type (in this case Cross Site Scripting) and allow you to enter your details on how to recreate the exploit. 

![](/files/Pasted%20image%2020240317130047.png)

Now if we navigate back into Faction and view the details we will see the exploit steps displayed in rich text. 

![](/files/Pasted%20image%2020240317130408.png)




