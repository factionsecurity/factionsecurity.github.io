## Introduction
Faction has an API similar to what you might find in BurpSuite Extensions. You can create custom modules in jar files and upload them to the Faction AppStore. Once uploaded, Faction will perform your custom processing when certain events are triggered like finalizing and assessment, creating a report, or failing a retest. 

You can even extend things like the Application Inventory Search so that it queries an external database to return results before scheduling assessments.


You can download an example [Extension here.](https://github.com/factionsecurity/Faction-Jira-Extension)

Below is a list of the current Hooks:

## Faction Extension APIs
### Application Inventory Extension
```java
public class MyPlugin extends BaseExtension implements com.faction.extender.ApplicationInventory{

	@Override
	public InventoryResult[] search(String arg0, String arg1) {

		return null;
	}
}
```
- Triggers on Assessment Scheduling and will then query external sources instead of the local database.
- Can search based on Application ID or Application name. It will return an InventoryResult Object (explained later)

### Assessment Manager Extension
```java
public class MyPlugin extends BaseExtension implements com.faction.extender.AssessmentManager{

	@Override
	public AssessmentManagerResult assessmentChange(Assessment arg0, List<Vulnerability> arg1, Operation arg2) {

		return null;
	}

}
```
Typical use case scenario: When an assessor finalizes an assessment this module can send all the vulnerabilities to another tracking system like JIRA and return the tracking numbers to Faction.

- Triggers on Assessment Create, Update, Delete, Finalized, Peer Review Created, Peer Review Complete, Peer Review Accepted
- Accepts the Triggered Assessment and List of vulnerabilities associated with the assessment.
- Returns AssessmentManagerResult, that is the updated Assessment and updated List of vulnerabilities
- If the return object is null Faction will not update locally

### Update Reports
```java
public class VulnerabilityBarChart extends BaseExtension implements com.faction.extender.ReportManager {

	@Override
	public String reportCreate(Assessment asmt, List<Vulnerability> vulns, String reportText) {

	return reportText;

}
```
This method triggers every time a report is created or regenerated. It can be used to for you to add custom variables to reports and update those variables with HTML. An example of this can be [found here](https://github.com/factionsecurity/Faction-Vulnerability-Bar-Chart) which demonstrates how to add bar charts to vulnerability reports. 

- Triggers on report create or regenerate
- Can update Text in reports
- Output can be HTML or raw text
- If returns null then nothing will be changed by this extension

### Vulnerability Manager Extension
```java
public class MyPlugin extends BaseExtension extends BaseExtension implements com.faction.extender.VulnerabilityManager{

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
```java
public class MyPlugin extends BaseExtension extends BaseExtension implements com.faction.extender.VerificationManager{

	@Override
	public void verificationChange(User arg0, Vulnerability arg1, String arg2, Date arg3, Date arg4, Operation arg5) {
		
	}
}
```

- Triggers on Pass, Fail, Cancel, Assigned
- Accepts the Triggered Assigned User, Vulnerability Assigned, Start and end dates for the verification.
- Returns the updated vulnerability

## Additional Resources
- [Building a JIRA Extension](/Extending%20FACTION/)