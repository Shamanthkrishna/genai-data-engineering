import pandas as pd
import google.generativeai as genai
from config.config import GEMINI_API_KEY
import os

def enrich_metadata(csv_file, out_path="outputs/reports/metadata_report.md"):
    df = pd.read_csv(csv_file)
    profile = df.describe(include="all").to_string()

    genai.configure(api_key=GEMINI_API_KEY)
    prompt = f"""
    You are a data analyst. Here is a dataset profile:
    {profile}
    Please write a short Markdown report with:
    - Data quality assessment (0-100 scale)
    - Business meaning of columns
    - Interesting insights
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    resp = model.generate_content(prompt)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write(resp.text)

    return out_path
