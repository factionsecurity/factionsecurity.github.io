## Introduction
Faction has an API similar to what you might find in BurpSuite Extensions. You can create custom modules in jar files and copy them to the server and Faction will automatically pick them up and do your custom processing on certain events.

You can extend things like Application Inventory Search so that it queries an external database to return results before scheduling assessments.

If you have configured custom fields you can write an extension to search another database and update things like application owner or other metadata about the application that Faction does not support by default.

You can download an example [Extension here.](https://github.com/factionsecurity/JiraPluginExample)

Below is a list of the current Hooks:

## Faction Extension APIs
### Application Inventory Extension
```java
public class MyPlugin implements com.fuse.extender.ApplicationInventory{

	@Override
	public InventoryResult[] search(String arg0, String arg1) {
		// TODO Auto-generated method stub
		return null;
	}
}
```
- Triggers on Assessment Scheduling and will then query external sources instead of the local database.
- Can search based on Application ID or Application name. It will return an InventoryResult Object (explained later)
### Assessment Manager Extension
```java
public class MyPlugin implements com.fuse.extender.AssessmentManager{

	@Override
	public Object[] assessmentChange(Assessment arg0, List<Vulnerability> arg1, Operation arg2) {
		// TODO Auto-generated method stub
		return null;
	}

}
```
Typical use case scenario: When an assessor finalizes an assessment this module can send all the vulnerabilities to another tracking system like JIRA and return the tracking numbers to Faction.

- Triggers on Assessment Create, Update, Delete, Finalized, Peer Review Created, Peer Review Complete, Peer Review Accepted
- Accepts the Triggered Assessment and List of vulnerabilities associated with the assessment.
- Returns an Object Array that is the updated Assessment and updated List of vulnerabilities
- If the return object is null Faction will not update locally

### Vulnerability Manager Extension
```java
public class MyPlugin implements com.fuse.extender.VulnerabilityManager{

	@Override
	public Vulnerability vulnChange(Assessment arg0, Vulnerability arg1, Operation arg2) {
		// TODO Auto-generated method stub
		return null;
	}
}
```
Typical use case scenario: When an assessor creates or updates a vulnerability the module can send the vulnerability to another tracking system like JIRA and return the tracking number to Faction.

- Triggers on Assessment Create, Update, Delete
- Accepts the Triggered Assessment and vulnerability that is being processed.
- Returns the updated vulnerability
- If the return object is null then Faction will not update locally

### Verification(Retest) Manager Extension
```
public class MyPlugin implements com.fuse.extender.VerificationManager{

	@Override
	public void verificationChange(User arg0, Vulnerability arg1, String arg2, Date arg3, Date arg4, Operation arg5) {
		// TODO Auto-generated method stub
		
	}
}
```

- Triggers on Pass, Fail, Cancel, Assigned
- Accepts the Triggered Assigned User, Vulnerability Assigned, Start and end dates for the verification.
- Returns the updated vulnerability

## Additional Resources
- [Building a JIRA Extension](/Extending%20FACTION/)