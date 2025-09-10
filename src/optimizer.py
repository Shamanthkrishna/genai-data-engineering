import google.generativeai as genai
from config.config import GEMINI_API_KEY
import os

def optimize_pipeline(code_file, out_path="outputs/reports/optimizations.md"):
    genai.configure(api_key=GEMINI_API_KEY)
    with open(code_file, "r") as f:
        code = f.read()

    prompt = f"""
    Analyze this Python ETL pipeline code and suggest optimizations:
    - Performance bottlenecks
    - Memory efficiency
    - Scalability improvements
    - Best practices
    ```python
    {code}
    ```
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    resp = model.generate_content(prompt)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write(resp.text)

    return out_path
