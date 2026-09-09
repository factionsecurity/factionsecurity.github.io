---
tags: [ Authentication, Core Features]
date: 2023-12-18
---
# Integrate Faction into OIDC Solutions
Faction seamlessly integrates with your existing enterprise authentication solutions, ensuring a smooth and secure user experience. Leveraging widely adopted solutions such as LDAP and OIDC, Faction effortlessly integrates into any enterprise environment. Our platform is designed to adapt to your authentication infrastructure, providing a hassle-free implementation process and enhancing the overall efficiency of your organization’s security framework. With Faction, you can trust in a unified and streamlined authentication experience tailored to your enterprise needs.

This article will walk through the steps needed to integrate [Faction](https://www.factionsecurity.com/) into [Google Auth](https://console.developers.google.com/), [Auth0](https://auth0.com/), or [Ping Identity](https://www.pingidentity.com/en.html).

## Google OIDC Setup
1. Log into your company’s [Google API Console](https://console.developers.google.com/).
2. Click on **Credentials** from the left navigation.
3. Click **+ Create Credentials** from the top navigation.
4. Select **OAuth Client ID.**
5. Select **Web Application** as the application type.
6. Name the application something specific like **Faction OIDC Integration**, but the name does not matter.
7. Under **Authorized redirect URLs**, click **+ ADD URI**.
8. Enter the domain of your Faction Instance and append **/oauth/callback?client_name=OidcClient** to the path. Example: If you used Faction to host the site, your URL would look like this:  
    https://furry-hyena-1111.factionsecurity.com/oauth/callback?client_name=OidcClient
9. Then click **Create**.
10. Take note of the **Client Id** and **Client Secret**. These will be used later in the Faction Admin section.

Your setup should look like the following:
![](files/Pasted%20image%2020231218082044.png)

## Auth0 OAuth Setup
1. Log into your [Auth0 Console](https://manage.auth0.com/dashboard/).
2. Select **Applications** in the left navigation.
3. Click **+ Create Application**.
4. Select **Regular Web Application.**
    ![](files/Pasted%20image%2020231218082151.png)
5. Name it something like **Faction OAuth Integration.**
6. Click **Create**.
7. Ignore the Quick Start screen and click **Settings**.
8. In the **Allowed Callback URLs**, enter the domain of your Faction Instance and append **/oauth/callback?client_name=OidcClient** to the path. **Example**: If you used [Faction](https://docs.factionsecurity.com/Managed%20FACTION%20Setup/) to host the site, your URL would look like: **https://furry-hyena-1111.factionsecurity.com/oauth/callback?client_name=OidcClient**
    ![](files/Pasted%20image%2020231218082323.png)
9. Take note of the **Client Id** and **Client Secret**. These will be used later in the Faction Admin.
10. Scroll down to the bottom and click **Advanced** and then **Endpoints**.
11. Take note of the **OpenID Configuration** URL.
    ![](files/Pasted%20image%2020231218082551.png)

## Ping Identity Setup
1. Log into the [Ping Identity Console](https://admin.pingone.com/web-portal/login).
2. Select Applications.
3. Add a New Application.
4. Give the Application a name like Faction.
5. Select OIDC Web App.
6. Click Save.
    ![](/files/Pasted%20image%2020241030210354.png)
7. Open the newly created application and select the Configuration tab:
   ![](/files/Pasted%20image%2020241030210859.png)
8. Click the Edit button in the upper right corner.
9. Scroll down to the Redirect URI Section and enter your Host Name with the path `/oauth/*`. (Example: `https://furry-hyena-1111.factionsecurity.com/oauth/*`)
10. Click Enable Redirect Patterns.
    ![](/files/Pasted%20image%2020241030211237.png)
11. Click Save.
12. Scroll up to the top of the configuration.
13. Expand __URLs__ and take note of the __OIDC Discovery Endpoint__. This will be used later in the __Configure Faction__ section.
14. Take note of the __Client Id__ and the __Client Secret__. These will be used in the __Configure Faction__ section.
15. Click the __Attribute Mappings__ tab.
16. Add email as an attribute.
    ![](/files/Pasted%20image%2020241030211944.png)
17. Click Save.

## Configure Faction
1. Log into **Faction** as an admin user.
2. Navigate to **Admin** -> **Users**.
3. In the **OAuth2.0 Configuration**, enter the __Client Id__ you noted earlier from either Auth0, Google, or Ping.
4. Enter the **Client Secret** you noted earlier.
5. Enter the **Discovery URL** as follows:
	1. **Google:** _https://accounts.google.com/.well-known/openid-configuration_  
	2. **Auth0:** Enter the **OpenID Configuration** URL you noted in step 11 above.
	3. **Ping**: Enter the __OIDC Discovery Endpoint__ from step 13 above.
6. Click **Save**.
![](files/Pasted%20image%2020231218082632.png)



## Adding an OAuth User
1. Under **Admin -> Users**, click **Add User.**
2. The username should be the part of the user’s email address before the @ symbol. If the email is **test.user@yourcompany.com**, then the username is **test.user**.
3. ⭐️**Leave the Password Field Blank.**⭐️
4. Enter the **First** and **Last** name.
5. Enter the **email** address that is used by the OAuth solution to authenticate the user.
6. Select **OAuth 2.0** as the Authentication Method.
7. Click **Save Changes**.

![](files/Pasted%20image%2020231218082756.png)

When the new user reaches the login screen, they can enter just their username without a password and click **Login**. Faction will redirect the user to the configured Authentication Provider and redirect back.

## Custom Sign-On URLs
You can bypass the username and password form by bookmarking the below URL. This ensures you don't need to enter a username just to be redirected to your SSO portal, where the user needs to enter their username again. The below URL will redirect directly to your configured SSO portal for OIDC.

```
https://YOURHOST/sso/oidc
```