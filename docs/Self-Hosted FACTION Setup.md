If you decide to self-host Faction instead of using the [Managed Solution](/Managed%20FACTION%20Setup/) then you will need to ensure you include the proper Environment variables so that Faction integrates into your environment.

## Requirements
- Tomcat 9
- Java 11
- Mongo 7
- maven

## Option 1:  Docker Compose
Download the code from GitHub and run the following commands
```
git clone git@github.com:factionsecurity/faction.git
cd faction
mvn clean compile war:war
docker-compose up --build
```
### Updating Faction
New releases can be found [here](https://github.com/factionsecurity/faction/releases). You can either pull a new release of Faction and build it yourself as shown above or If you don't want to perform the Maven install you can download the `faction.war` file directly and put it into the targets folder. 

## Option 2: Install Tomcat and Mongo
_Check back, instructions will be updated soon_

## Custom Environment Variables
```
## Mongo Database configs 

FACTION_MONGO_HOST=127.0.0.1. #requireed 
FACTION_MONGO_DATABASE=faction #required 
FACTION_MONGO_USER=faction_mongo_user #optional 
FACTION_MONGO_PASSWORD=faction_mongo_pass #optional 
FACTION_MONGO_AUTH_DATABASE=admin #optional 

FACTION_SECRET_KEY=faction_encryption_key #required 

FACTION_REPORT_STORAGE=aws #optional 
FACTION_BUCKET_NAME=your-bucket #optional 
FACTION_TIER=teams #required 
FACTION_USERS=100 #optional 

FACTION_SMTP_SERVER=smtp.server.com #optional 
FACTION_SMTP_USER=sysadmin #optional 
FACTION_SMTP_PORT=587 #optional
```

### Mongo Database Variables

- **FACTION_MONGO_HOST** (_Required_):  
    This is the hostname or ip address where your mongo database i location
- **FACTION_MONGO_DATABASE** (_Required_):  
    The name of the mongo database. This can be anything you want. On initial loading of the application it will create the database and all collections.
- **FACTION_MONGO_USER** (O_ptional_):  
    If you use authentication (and you should) then this user has access to the database.
- **FACTION_MONGO_PASSWORD** (_Optional_):  
    Only required if you use the FACTION_MONGO_USER environment variable.
- **FACTION_MONGO_AUTH_DATABASE** (Optional):  
    The default authentication database is **admin.** If you want to use another then you can use this variable.
### Other Variables
- **FACTION_SECRET_KEY** (_Required_):  
    This is the key used for all symmetric key encryption.
- **FACTION_REPORT_STORAGE** (_Optional_):  
    This variable has two options: **local** or **aws**. If you include **aws** then you also need to set **AWS_ACCESS_KEY_ID** and **AWS_SECRET_ACCESS_KEY** and create the an s3 bucket location in AWS. _You can also use IAM permissions instead of including the AWS Keys._   
    When using **local**  the default directory location is **/opt/faction.** If this variable is not set, **local** will be used as default.
- **FACTION_BUCKET_NAME** (_Optional_):  
    S3 Bucket Name to to store Faction files.
- **FACTION_TIER** (_Required_):  
    Only use the value **team** here
- **FACTION_USERS** (_Required_):  
    The user limit. you can set this to any value that makes sense for your organization.

### Email Variables
These settings (**FACTION_SMTP_SERVER, FACTION_SMTP_USER< FACTION_SMTP_PORT**) are just used for the initial setup of Faction. They will be overridden when you save or test emails in the admin settings pages. This is useful for doing deployments in Kubernetes or ECS.