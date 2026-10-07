import re

subject = input_data.get('subject', '') or ''
body = input_data.get('body', '') or ''
text = (subject + " " + body).lower()

keywords = re.findall(r'\b\w{3,}\b', body)

positive_words = [
    'appreciate','happy','great','love','good','improve','reliable','trustworthy', 'affordable','well-designed','easy','impressed','fantastic','wonderful','excited', 'excellent', 'fantastic', 'helpful', ]

negative_words = [
    'complaint','problem','angry','bad','hate','terrible','urgent','immediate', 'unresponsive','disappointed','frustrated','frustrating','not satisfied','malfunction',
    'trouble','delay','awful','unclear','overcharged','refund','cannot','cant','no access',
    'lost access','important','necessary', 'broken', 'escalation', 'escalate', 'unacceptable']

positive_score = sum(word in text for word in positive_words)
negative_score = sum(word in text for word in negative_words)

if positive_score > negative_score:
    sentiment = "positive"
elif negative_score > positive_score:
    sentiment = "negative"
else:
    sentiment = "neutral"

urgency = "high" if ("urgent" in text or "immediate" in text) else "normal"

output = {
    "subject": subject,
    "body": body,
    "sentiment": sentiment,
    "urgency": urgency
}
