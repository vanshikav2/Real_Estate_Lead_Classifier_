from typing import Dict
from llm import classify_lead
from emailing import send_email

def deduplicate_lines(text):
    seen = set()
    lines = []
    for line in text.splitlines():
        if line.strip() and line not in seen:
            lines.append(line)
            seen.add(line)
    return "\n".join(lines)

def lead_agent(lead: Dict):
    llm_output = classify_lead(lead)
    print("\nLLM Suggestion:\n", llm_output, "\n")

    action = "IGNORE"
    subject = None
    body = None

    for line in llm_output.splitlines():
        line_upper = line.upper()
        if "ACTION:" in line_upper and "SEND_EMAIL" in line_upper:
            action = "SEND_EMAIL"
        elif "SUBJECT:" in line_upper:
            subject = line.split(":", 1)[1].strip()
        elif "BODY:" in line_upper:
            body = line.split(":", 1)[1].strip()
            body = body.replace("\\n", "\n")
            body = deduplicate_lines(body)
            import os

            # Replace placeholders with SMTP user info
            smtp_user = os.getenv("SMTP_USER", "you@example.com")
            body = body.replace("[Your Name]", smtp_user.split("@")[0])  # username before @
            body = body.replace("[Your Contact Information]", smtp_user)




    if action == "SEND_EMAIL" and lead.get("email") and subject and body:
        send_email(lead["email"], subject, body)


