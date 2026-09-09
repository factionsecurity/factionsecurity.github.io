---
tags: [Authentication, Core Features]
date: 2025-05-28
---
## Overview
This tutorial will walk you through the steps required to set up Faction with your Microsoft Entra ID Single Sign-On using SAML.

## Configuring Entra ID in Azure

1. Open the Azure Console and navigate to "Entra ID".
   ![](/files/Pasted%20image%2020250528231939.png)
2. Navigate to Enterprise Applications.
3. Click "New Application"
4. Click "Create your own application."
5. Enter a name (e.g. Faction SAML) and select the "Integrate any other application you don't find in the gallery (Non-gallery)" radio button.
6. Click Manage->"Single Sign On", then select SAML
   ![](/files/Pasted%20image%2020250528232758.png)
7. Click 'Edit' under "Basic SAML Configuration"
8. Under Identifier (Entity ID) enter the following URLs:
   - `https://yourfactionurl.com/saml2/callback?client_name=SAMLClient`
   - `https://yourfactionurl.com/saml2/callback`
9. Under "Reply URL (Assertion Consumer Service URL)", add the following reply URLs:
   - `https://yourfactionurl.com/saml2/callback?client_name=SAMLClient`
   - `https://yourfactionurl.com/saml2/callback`
10. If your config looks like the image below, then click 'Save'.
    ![](/files/Pasted%20image%2020250529222514.png)
11. Now navigate to "Single Sign On" and copy the "App Federation Metadata Url". This will be used in the next section.
    ![](/files/Pasted%20image%2020250529083833.png)

## Finish Configuration in FACTION
With the Federation URL copied, you are now ready to finish the configuration on the Faction side.
1. Log in to Faction as an admin
2. Navigate to Administration->Users
3. Scroll to the bottom and enter the URL we copied from step 11 above into the "App Federation Metadata Url" input box.
4. Click Save

## Configure a User for SAML Authentication
1. Log in to Faction as an admin
2. Navigate to Administration->Users
3. Click Add User
4. Set the following parameters:
   - Set the username to the first part of the email address.
   - Enter the first and last name of the user
   - Leave the password blank
   - Set the email address. It MUST match the email address of the user managed in Entra ID.
   - Set the "Authentication Method" to SAML2
     ![](/files/Pasted%20image%2020250529222945.png)
5. Click Save
   
## Login with SAML
SAML users only need to enter their username and submit login. Faction will automatically redirect the user to the SSO login form.

## Custom Sign-On URLs
You can bypass the username and password form by bookmarking the below URL. This ensures you don't need to enter a username just to be redirected to your SSO portal, where the user needs to enter their username again. The below URL will redirect directly to your configured SSO portal for SAML.

```
https://YOURHOST/sso/saml
```

