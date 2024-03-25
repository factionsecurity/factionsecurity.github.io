---
tags: [CVSS, Vulnerability, Core Features]
date: 2024-03-14
---

Native: <img alt="Static Badge" src="https://img.shields.io/badge/Since-1.0-blue?style=flat">

CVSS: <img alt="Static Badge" src="https://img.shields.io/badge/Since-1.2-blue?style=flat">

FACTION's severity rankings are easily customizable to how you perform assessments. You can even create different severity options for the type of assessment. 

FACTION has 3 options to choose:

1. Native Severity - This is simply High, Medium, Low, etc type rankings. Faction let you set up to 10 levels and can rename them to anything that works for your process. 
2. CVSS 3.1 - This option enables [First.org CVSS 3.1 Severity Scoring](https://www.first.org/cvss/calculator/3.1) and *was introduced in FACTION 1.2*
3. CVSS 4.0 = This option enables [First.org CVSS 4.0 Scoring](https://www.first.org/cvss/calculator/3.1) and *was introduced in FACTION 1.2*

## Native Severity Ranking
![](files/Pasted%20image%2020240315000731.png)
By default, assessments are enabled with Native Severity Ranking. You can choose up to 10 levels. The most common severity names are pre-populated when you install FACTION. You are free to change these names to anything you wish. If your process uses a different nomenclature then you can change `Critical` to  `P1` and `High` to `P2` for example. 

You can find this setting in Templates -> Default Vulnerabilities.

When Native Severity Ranking is enabled, the following options are available when adding a new vulnerability:
![](files/Pasted%20image%2020240315002524.png)

## Changing the Severity Scoring System
The severity scoring system is set for each assessment type. You can change this or create new assessment types by navigating to Admin -> Settings:

![](files/Pasted%20image%2020240315001346.png)

Notice above that each assessment has a different scoring system. To change the assessment scoring system then simply click the `edit` button an select the scoring system from the drop-down.

![](files/Pasted%20image%2020240315001514.png)

## CVSS 3.1 and 4.0 Severity Ranking
When changing the scoring system to CVSS 3.1 or 4.0, it changes the vulnerability UI and adds CVSS Calculators to the page. 

![](files/Pasted%20image%2020240315002736.png)

Clicking on the calculator button next to the CVSS Vector will open a dialog that will build the CVSS vector for you and update the score. 
![](files/Pasted%20image%2020240315003032.png)


