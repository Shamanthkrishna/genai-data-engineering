import google.generativeai as genai
from config.config import GEMINI_API_KEY
import os

def generate_docs(code_file, out_path="docs/generated/pipeline_doc.md"):
    genai.configure(api_key=GEMINI_API_KEY)
    with open(code_file, "r") as f:
        code = f.read()

    prompt = f"""
    You are a technical writer. Generate clear Markdown documentation for this ETL pipeline:
    ```python
    {code}
    ```
    Include: Extract, Transform, Load steps and a Mermaid diagram.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    resp = model.generate_content(prompt)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write(resp.text)

    return out_path
