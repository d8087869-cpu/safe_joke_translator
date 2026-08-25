import os
import requests
from dotenv import load_dotenv


load_dotenv()

DEEPL_API_URL = os.getenv("DEEPL_API_URL")
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")


def translate_joke(joke, target_language):
    data = {
        "text": joke,
        "source_lang": "EN",
        "target_lang": target_language.upper()
    }

    headers = {
        "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"
    }

    response = requests.post(
        DEEPL_API_URL,
        data=data,
        headers=headers
    )
    return response.json()

def extract_translation(api_data):
    return api_data["translations"][0]["text"]