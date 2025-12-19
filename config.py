import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# SMTP
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "user")
SMTP_PASS = os.getenv("SMTP_PASS", "pass")
SMTP_FROM = os.getenv("SMTP_FROM", "noreply@example.com")
