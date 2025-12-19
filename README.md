# Real Estate Lead Classifier 

## Overview

This project implements a **Lead Qualification Agent** for the real estate domain. The agent uses a **Large Language Model (LLM)** to classify incoming leads as **BUY**, **RENT**, or **IGNORE**, and optionally sends personalized emails to valid leads.  

The agent demonstrates a **GenAI-controlled workflow**, where the LLM determines the control flow of the automation, including lead classification and next actions. The system is modular, production-ready, and easy to extend.

---

## Features

- Classifies leads based on **budget, location, and message content**.
- Generates **personalized email messages** for leads.
- Automatically sends emails for valid leads.
- Deduplicates repeated lines in LLM responses.
- Validates email addresses and ignores invalid ones (treated as spam).
- LLM-driven control flow: all decisions come from the model's output.

---

## Tech Stack

- **Python 3.12+**
- **OpenAI API** (LLM for classification)
- **SMTP / Email** for automated messaging
- Environment variables via **.env** file

---

## Project Structure

GenAI_Model
|
- agent.py # Main agent logic: parses LLM output, validates email, triggers actions
- emailing.py # Handles sending emails via SMTP
- llm.py # Interacts with OpenAI LLM to classify leads
- main.py # Entry point with sample leads to run the agent
- requirements.txt # Python dependencies
- .env # Environment variables (API keys, SMTP credentials)




---

## Setup Instructions

1. **Clone the repository**

```bash
git clone <repository-url>
cd GenAI_Model
Install dependencies

python -m pip install -r requirements.txt
```

2. **Set up environment variables**

Create a .env file in the project root with the following keys:

OPENAI_API_KEY=<your_openai_api_key>
SMTP_USER=<your_email_address>
SMTP_PASS=<your_email_password_or_app_password>
SMTP_FROM=<from_email_for_sending>
SMTP_HOST=<smtp_host, e.g., smtp.gmail.com>
SMTP_PORT=<smtp_port, e.g., 587>


Note: For Gmail, you may need to generate an App Password to allow SMTP access.

3. **Run the agent**
```bash
python main.py
```

## Usage Example
```bash 
from agent import lead_agent

lead = {
    "name": "Ava",
    "email": "ava@example.com",
    "budget": 2000,
    "location": "Brampton",
    "message": "Looking to rent a 2-bedroom apartment starting February."
}

lead_agent(lead)
```

## Assumptions

The LLM (GPT-4o-mini) is used for lead classification and email suggestions.

Leads without a valid email address are ignored and treated as potential spam.

The system assumes correct SMTP credentials are provided in .env.

Emails are sent in plain text format; placeholders [Your Name] and [Your Contact Information] are automatically replaced by the SMTP user and agent name.

This agent demonstrates a learning example for GenAI automation and is not intended for production-scale deployment without additional security, logging, and error-handling measures.