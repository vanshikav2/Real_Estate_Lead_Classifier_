import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

SYSTEM_PROMPT = """
You are a real estate lead qualification agent.
Classify leads as BUY, RENT, or IGNORE.
Decide if an email should be sent.
Return plain text like:

CATEGORY: BUY
ACTION: SEND_EMAIL
SUBJECT: ...
BODY: ...
REASON: ...
"""

def classify_lead(lead: dict) -> str:
    user_msg = f"Lead info:\nName: {lead.get('name')}\nBudget: {lead.get('budget')}\nLocation: {lead.get('location')}\nMessage: {lead.get('message')}"
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()
