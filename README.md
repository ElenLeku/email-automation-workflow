# email-automation-workflow
This project automates email handling for a hypothetical company using Zapier, a custom Python sentiment-analysis script, and an LLM for tailored, immediate responses. Incoming emails are analyzed for sentiment and routed intelligently to reduce manual workload and imporve responce efficiency. 

# how it works
1. Trigger: New email received
2. Python sentiment analysis - a custom script processes the subject + body and classifies the message as negative, neutral or positive. Using keyword scoring and logic to determine sentiment and urgency.
3. Conditional routing based on sentiment: Negative emails -> forwarded to the correct department for human review. Ensures human attention for dissatisfied or urgent messages. Neutral or positive emails -> automatically answered using an LLM, generating a personalized, context-aware response.
4. LLM response generation: depending on the subject + body of the incoming email, a dedicated LLM with specific promopting will create the appropriate response, using data from its knowledge base and send it to the original sender.

# key features
- Custom Python sentiment analysis
- Intelligent routing based on message tone
- AI-generated email replies
- Multi-step workflow combining Python + Zapier + LLM
- Reduces manual inbox management
- Scalable and adapatable to real business environments

# tech stack 
- Python (sentiment analysis logic)
- Zapier (workflow automation)
- Zapier AI Actions (LLM response generation)
- Outlook (email handling)
- Paths & Filters (conditional logic)

# repository contents
- sentiment_analysis.py - Python script used inside Zapier
- zapier_flow/ - screenshots of the workflow


# notes
This project demonstrates how AI-powered automation and custom Python logic can reduce manual workload, and maintain consisten response quality. The workflow can be adapted to real companies with minimal changes.
