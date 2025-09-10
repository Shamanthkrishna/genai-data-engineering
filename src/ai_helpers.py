import google.generativeai as genai
from config.config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

def generate_text(prompt: str, model="gemini-1.5-flash"):
    """
    Generate text using Gemini API
    """
    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt)
    return response.text
