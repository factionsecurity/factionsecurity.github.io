Faction can extend its functionality on the server side. If you are familiar with writing BurpSuite extensions then this process should be somewhat familiar to you. If you are not it’s OK. We will walk through the specifics below.

In this example, we will create a JIRA plugin that will create issues for each vulnerability when the assessment is finalized.

The source code for this example can be [downloaded here](https://github.com/factionsecurity/JiraPluginExample).

## Faction Dev Environment
1.  Create a new Eclipse Maven Java Project
2. Add the following lines to your _pom.xml_ file to enable the Faction Extendar API. This adds the Extendar API Repository location, the Extendar Library, and configures the build plugin, and Manifest file.
```xml
<repositories>
   <repository>
      <id>FactionExtender</id>
      <url>https://github.com/factionsecurity/faction-extender/raw/mvn-repo/</url>
      <snapshots>
         <enabled>true</enabled>
         <updatePolicy>always</updatePolicy>
      </snapshots>
   </repository>
</repositories>
<dependencies>
   <dependency>
      <groupId>FactionExtender</groupId>
      <artifactId>FactionExtender</artifactId>
      <version>1.1</version>
   </dependency>
</dependencies>
<build>
   <plugins>
      <plugin>
         <artifactId>maven-assembly-plugin</artifactId>
         <configuration>
         <descriptorRefs>
            <descriptorRef>jar-with-dependencies</descriptorRef>
         </descriptorRefs>
         <archive> 
            <manifestEntries>
               <Import-Library>org.faction.JiraPlugin</Import-Library>
            </manifestEntries>
         </archive>
         </configuration>
       </plugin>
   </plugins>
</build>
```
The _maven-assembly-plugin_ contains the manifest entries which is important for Faction to be able to find the correct class files to run. You will need to update the **Import-Library** directive to point to your class.

## Create The Jira Plugin Class
Create a Class named **JiraPlugin** in _src/main/java_. This class will implement  _com.fuse.extender.AssessmentManager_ as shown below. This code will trigger whenever a change happens to an assessment. You can use the **Operation** enum to control what happens as different events change the assessment.

```java
public class JiraPlugin implements com.fuse.extender.AssessmentManager{
     @Override
     public Object[] assessmentChange(Assessment assessment, List<Vulnerability> vulnerabilities, Operation arg2) {
            return new Object [] {assessment, vulnerabilities};
     }
}
```

Note that above it returns **Object [] {assessment, vulnerabilities}.** This will update Faction’s database if the values change when this function returns. If you Return **null** it will NOT update Faction and only just send/process information.

## Putting It All Together
Now we have a basic functional block of code we need to make it perform the action of sending all vulnerabilities to Jira only when the assessment is finalized. To do this we create an if statement that checks the Operation enum equals Finalized.

```java
import com.fuse.elements.Assessment;
import com.fuse.elements.Vulnerability;

public class JiraPlugin implements com.fuse.extender.AssessmentManager{

	@Override
	public Object[] assessmentChange(Assessment assessment, List<Vulnerability> vulns, Operation opcode) {
		
		if(opcode == Operation.Finalize) {
			//Integration into vulnerability management system
			for(Vulnerability vuln : vulns) {
				//this can update vulns and send the updated values back into Faction
				String issueId = sendVulnerbilityToJira(vuln);
				if(issueId != null) {
					vuln.setTracking(issueId);
				}
			}
		}
		return new Object [] {assessment, vulns};
	}
}


```

Now we just need to add the following supporting functions to send the issues to Jira using their [REST API](https://docs.atlassian.com/software/jira/docs/api/REST/8.9.1/). **Note: To use this code you need to update the Environment Variables to use your Jira Hostname and API key. You also need to update the Project key to match your projects.**

```java
import java.util.Base64;
import java.util.List;

import com.fuse.elements.Assessment;
import com.fuse.elements.Vulnerability;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

public class JiraPlugin implements com.fuse.extender.AssessmentManager{

	@Override
	public Object[] assessmentChange(Assessment assessment, List vulns, Operation opcode) {
		
		if(opcode == Operation.Finalize) {
			//Integration into vulnerability management system
			for(Vulnerability vuln : vulns) {
				//this can update vulns and send the updated values back into Faction
				String issueId = sendVulnerbilityToJira(vuln);
				if(issueId != null) {
					vuln.setTracking(issueId);
				}
			}
		}
		return new Object [] {assessment, vulns};
	}
	
	public String sendVulnerbilityToJira(Vulnerability vuln) {
		
		JSONObject issueType = new JSONObject();
		issueType.put("name", "Bug");
		
		JSONObject project = new JSONObject();
		project.put("key", "KAN"); //Change this
		
		JSONObject fields = new JSONObject();
		fields.put("summary", vuln.getName());
		fields.put("description", vuln.getDescription());
		fields.put("project", project);
		fields.put("issuetype", issueType);
		
		JSONObject issue = new JSONObject();
		issue.put("fields", fields);
		String jiraHost = System.getenv("JIRA_HOST");
		String jiraURL = String.format("%s%s", jiraHost, "rest/api/2/issue/");
		return httpPost(jiraURL, issue);
	}
	
	private String base64(String data) {
		return "Basic " +Base64.getEncoder().encodeToString(data.getBytes());
	}
	
	private String httpPost(String url, JSONObject payload) {
		HttpClient httpClient = HttpClientBuilder.create().build();
		String apiKey = System.getenv("JIRA_API_KEY");
		try {
		    HttpPost request = new HttpPost(url);
		    StringEntity params = new StringEntity(payload.toJSONString());
		    request.addHeader("content-type", "application/json");
		    request.addHeader("Authorization", base64(apiKey));
		    request.setEntity(params);
		    HttpResponse response = httpClient.execute(request);
		    if( response.getStatusLine().getStatusCode() == 201) {
		    	String json = EntityUtils.toString(response.getEntity());
		    	JSONParser parser = new JSONParser();
		    	JSONObject jsonObj = (JSONObject) parser.parse(json);
		    	return (String) jsonObj.get("id");
		    }else {
		    	return null;
		    }
		} catch (Exception ex) {
			ex.printStackTrace();
			return "";
		} 
		
	}
}
```

## Install It In Your Faction

Build the jar file by running:
```
mvn clean compile assembly:single
```

This will create a jar file named **JiraPlugin-0.0.1-SNAPSHOT-jar-with-dependencies.jar** in your ./target folder. 

To run it on Faction, you need to copy **JiraPlugin-0.0.1-SNAPSHOT-jar-with-dependencies.jar** into the **/opt/faction/modules/** folder on your server. The Faction web server with automatically pick up this change without restarting and will execute your custom code when when the assessment is finalized. 

Now when an assessment is finalized it will add All the findings to JIRA as shown in the following screenshot:

![](files/Pasted%20image%2020231218085522.png)