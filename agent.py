from typing import Dict
from llm import classify_lead
from emailing import send_email
import os

USER_NAME = "Vanshika" # Write the agent name
YOUR_COMPANY = "ABC Real Estate Agency"  # Your agency name



def deduplicate_lines(text):
    " this function is to delete the repetitive lines"
    seen = set()
    lines = []
    for line in text.splitlines():
        if line.strip() and line not in seen:
            lines.append(line)
            seen.add(line)
    return "\n".join(lines)

def lead_agent(lead: Dict):
    " This is the main agent where the classified lead is assembled and email is sent accordingly"
    llm_output = classify_lead(lead)

    action = "IGNORE"
    subject = None
    body_lines = []
    capture_body = False

    for line in llm_output.splitlines():
        line_upper = line.upper()
        if "ACTION:" in line_upper and "SEND_EMAIL" in line_upper:
            action = "SEND_EMAIL"
        elif "SUBJECT:" in line_upper:
            subject = line.split(":", 1)[1].strip()
        elif "BODY:" in line_upper:
            capture_body = True
            # Add the rest of the line after 'BODY:' to body_lines
            body_lines.append(line.split(":", 1)[1].strip())
        elif line_upper.startswith("CATEGORY:") or line_upper.startswith("REASON:"):
            capture_body = False
        elif capture_body:
            # add all subsequent lines until next section
            body_lines.append(line)

    body = "\n".join(body_lines)
    body = body.replace("\\n", "\n")
    body = deduplicate_lines(body)

    # Replace placeholders with agent name and SMTP info
    smtp_user = os.getenv("SMTP_USER", "you@example.com")
    body = body.replace("[Your Name]", USER_NAME)
    body = body.replace("[Your Company]", YOUR_COMPANY)
    body = body.replace("[Your Contact Information]", smtp_user)

    print("\nLLM Suggestion:\n", llm_output, "\n")

    if action == "SEND_EMAIL" and lead.get("email") and subject and body:
        send_email(lead["email"], subject, body)


