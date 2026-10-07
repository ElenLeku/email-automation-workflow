# screenshots of workflow
The zapier_flow/ folder contains visual documentation of the automation:

- Full workflow overview: complete view of the entire Zap, showing how incoming emails move through the sentiment analysis, routing logic, and automated responses.
- Python sentiment analysis: a close-up of the "Code by Zapier" action where the custom Python script processes the email content and returns a sentiment score.
- Positive / Neutral path: screenshots showing the branch where emails with positive or neutral sentiment triggen an LLM-generated response that is sent directly back to the sender.
- Negative path: screenshots showing the branch where negative sentiment triggers escaltion to the appropriate department for human reveiw.
- Example input & output: a sample email prompt and the AI-generated response, demonstrating how the system handles real messages.

These screenshots provide a clear visual reference for how the automation works end-to-end. 
