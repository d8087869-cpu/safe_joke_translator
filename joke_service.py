import os 
import requests
from dotenv import load_dotenv

load_dotenv()

JOKE_API_URL = os.getenv("JOKE_API_URL")

def get_joke():
    params = {
        "safe-mode": "",
        "blacklistFlags": "nsfw,religious,political,racist,sexist,explicit",
        "type": "single"}
    
    response = requests.get(JOKE_API_URL, params=params)

    return response.json()

def is_safe_joke(joke_data):
    if joke_data.get("error"):
        return False

    if joke_data.get("type") != "single":
        return False

    if not joke_data.get("joke"):
        return False

    flags = joke_data.get("flags", {})

    required_flags = [
        "nsfw",
        "religious",
        "political",
        "racist",
        "sexist",
        "explicit"
    ]

    for flag in required_flags:
        if flags.get(flag):
            return False

    return True


def get_safe_joke():
    for attempt in range(3):
        joke_data = get_joke()

        if is_safe_joke(joke_data):
            return joke_data

    return None


def extract_joke_data(api_data):
    joke_data = {
        "joke": api_data["joke"],
        "category": api_data["category"],
        "joke_id": api_data["id"],
        "language": api_data["lang"]
    }

    return joke_data


def analyze_joke(joke):
    analysis = {
        "characters": len(joke),
        "words": len(joke.split())
    }
    return analysis