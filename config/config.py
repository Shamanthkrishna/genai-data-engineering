import os

# Read Gemini API key from env; keep file free of secrets
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
