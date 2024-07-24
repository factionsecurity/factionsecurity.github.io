![image](https://github.com/user-attachments/assets/b181ae83-d6ff-40ef-868d-9e637c7fde5f)---
tags: [ Authentication, Core Features]
date: 2023-12-18
---
# Integrate Faction into OAuth Solutions
Faction seamlessly integrates with your existing enterprise authentication solutions, ensuring a smooth and secure user experience. Leveraging widely adopted solutions such as LDAP and OAuth, Faction effortlessly integrates into any enterprise environment. Our platform is designed to adapt to your authentication infrastructure, providing a hassle-free implementation process and enhancing the overall efficiency of your organization’s security framework. With Faction, you can trust in a unified and streamlined authentication experience tailored to your enterprise needs.

The article will walk through the steps needed to integrate [Faction](https://www.factionsecurity.com/) into [Google Auth](https://console.developers.google.com/) or [Auth0](https://auth0.com/).

## Google OAuth Setup
1. Log into your company’s [Google API Console](https://console.developers.google.com/).
2. Click on **Credentials** from the left navigation.
3. Click **+ Create Credentials** from the top navigation.
4. Select **OAuth Client ID.**
5. Select **Web Application** as the application type.
6. Name the application something specific like **Faction OAuth Integration.** But the name does not matter.
7. Under **Authorized redirect URLs** click **+ ADD URI**.
8. Enter the domain of your Faction Instance and append **/oauth/callback?client_name=OidcClient** to the path. Example: If you used Faction to host the site your URL would look like this:  
    https://furry-hyena-1111.factionsecurity.com/oauth/callback?client_name=OidcClient
9. Then Click **Create**.
10. Take Note of the **Client Id** and **Client Secret**. This will be used later in the Faction Admin Section.

Your Setup should look like the following:
![](files/Pasted%20image%2020231218082044.png)

## Auth0 OAuth Setup
1. Log into your [Auth0 Console](https://manage.auth0.com/dashboard/).
2. Select **Applications** in the left navigation.
3. Click **+ Create Application**
4. Select **Regular Web Application.**
    ![](files/Pasted%20image%2020231218082151.png)
5. Name it something like **Faction OAuth Integration.**
6. Click **Create**.
7. Ignore the Quick Start screen and Click **Settings**.
8. In the **Allowed Callback URLs**, enter the domain of your Faction Instance and append **/oauth/callback?client_name=OidcClient** to the path.  **Example**: If you used [Faction](https://docs.factionsecurity.com/Managed%20FACTION%20Setup/) to host the site your URL would look like: **https://furry-hyena-1111.factionsecurity.com/oauth/callback?client_name=OidcClient**
    ![](files/Pasted%20image%2020231218082323.png)
9. Take Note of the **Client Id** and **Client Secret**. This will be used later in the Faction Admin.
10. Scroll down to the bottom and Click **Advanced** and then **Endpoints**
11. Take note of the **OpenId Configuration** URL
    ![](files/Pasted%20image%2020231218082551.png)


## Entra Id Setup  
**Proper roles are required to register Enterprise Application (at least Cloud Application Administrator).  
1. Log into your [Entra Id Admin Panel](https://entra.microsoft.com/#home)  
2. Go to the **Applications** -> **Enterprise Applications** -> **All Applications**  
(follow [this](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal))  
3. Create your own application (non-gallery)  
![image](https://github.com/user-attachments/assets/c5951b6a-53e1-4a43-b6c2-07ee0c0a375d)  
4.  Go to *App Registrations** and select just created app  
![image](https://github.com/user-attachments/assets/8f429f76-5fc1-4d6d-a214-410f89d57696)  
5.  Generate secret for App  
![image](https://github.com/user-attachments/assets/231d2be5-6e06-4503-bdaf-253853af4f65)  
6.  Obtain for Faction:  
   - Application Id (Client Id) of an app  
   - Entra URL for OIDC, commonly: *https://login.microsoftonline.com/$(tenantId)/v2.0/.well-known/openid-configuration*  
   - Application Secret just created  
7. Set up proper Platform configuration. Go to **Authentication** and Add a platform  
    - WebApplication (URL: *https://example.factionsecurity.com/oauth/callback?client_name=OidcClient* - change example for Your faction tenant name)  
![image](https://github.com/user-attachments/assets/06b47005-e8b6-4aa3-9003-bf1d66ff8679)  
![image](https://github.com/user-attachments/assets/74adc92f-d571-44af-82f1-d0a5a93992e2)  
8. In the Enterprise application panel assign proper users (or group) to the Enterprise application.
  
## Configure Faction
1. Log into **Faction** as an admin user.
2. Navigate to **Admin** -> **Users**.
3. In the **OAuth2.0 Configuration** enter the Client Id you noted earlier from either Auth0 or Google.
4. Enter the **Client Secret** you noted earlier.
5. Enter the **Discovery URL** as follows:**Google:** _https://accounts.google.com/.well-known/openid-configuration_  
    **Auth0:** Enter the **Open Id Configuration** URL you noted in step 11 above.
6. Click **Save**
![](files/Pasted%20image%2020231218082632.png)

## Adding an OAuth User
1. Under **Admin -> Users**, Click **Add User.**
2. The Username should be part of the user’s email address before the @ symbol. If the email is **test.user@yourcompany.com** then the username is **test.user**
3. ⭐️**Leave the Password Field Blank.**⭐️
4. Enter the **First** and **Last** name.
5. Enter the **email** address that is used by the OAuth solution to authenticate the user.
6. Select **OAuth 2.0** as the Authentication Method.
7. Click **Save Changes**.

![](files/Pasted%20image%2020231218082756.png)

When the new user reaches the Login Screen they can enter just their username without a password and click **Login**. Faction will redirect the user to the configured Authentication Provider and redirect back.
