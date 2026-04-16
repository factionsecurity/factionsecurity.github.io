---
tags: [LLM, AI, Enterprise]
date: 2026-04-16
---

Below are the steps to create an Azure OpenAI endpoint that can be used with Faction' AI capabilities.

1. Create an AI Foundry Instance if you have not already done so. Skip to **step 12** if this part is already complete.  
2. You have the option to use different types of AI subscriptions. We are using our Copilot subscription for this instance
   ![](/files/Pasted%20image%2020260416162533.png)
3. Click Click Review and Create
4. Click Create
5. Click "Go to Resource". This should take you to the AI Foundry Portal
   ![](/files/Pasted%20image%2020260416162800.png)
6. Once you at the Foundry Portal Click "Model Catalog" in the left side bar. 
   ![](/files/Pasted%20image%2020260416162913.png)
7. Search for a model like `gpt-4o` and select it. *Note some models require additional approvals to use.* 
8. Click "Use this Model"
	![](/files/Pasted%20image%2020260416162926.png)
9. Name it something meaningful like `faction-gpt-4o`
   ![](/files/Pasted%20image%2020260416162944.png)
10. Click "Create Resource and deploy"
11. Once deployed you should be able to see its settings and get your API Key. Leave this page open and navigate to Faction's AI configs in Admin (Admin->AI Config)
12. Add a new LLM Config and map the attributes as shown below:
    ![](/files/Pasted%20image%2020260416162951.png)
13. Now click "Test Connection" to verify it works
    
    ![](/files/Pasted%20image%2020260416162956.png){ align=center }

Now you are ready to use all of Factions AI features like automatic report generation, automated checklists, and executive summary generation. 