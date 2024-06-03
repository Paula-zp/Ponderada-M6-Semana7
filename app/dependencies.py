import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_URL = os.getenv("url da api do gemini (não fiz)")
GEMINI_API_KEY = os.getenv("key da api (não fiz)")

# Função responsável por gerar o conteúdo de uma história
def generate_story_content(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post(GEMINI_API_URL, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    return result['choices'][0]['text'].strip()
