import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_invoice(text: str):
    prompt = f"""
    Analyze the following invoice for any silent price increases or unusual vendor charges. 
    Return:
    - Summary of findings
    - Line-item flags (item, issue)
    
    Invoice content:
    {text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )

    content = response.choices[0].message["content"]
    # Optional: parse content into JSON structure
    return {
        "summary": content.split("\n")[0],
        "flags": [
            {"line": line, "reason": "Flagged by model"} 
            for line in content.split("\n")[1:] if line.strip()
        ]
    }
