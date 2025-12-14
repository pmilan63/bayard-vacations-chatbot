import json
from pathlib import Path

INTENTS_PATH = Path(__file__).parent / "intents.json"

with open(INTENTS_PATH, "r", encoding="utf-8") as file:
    INTENTS = json.load(file)


def get_response(user_message: str) -> str:
    user_message = user_message.lower()

    for intent in INTENTS.values():
        for keyword in intent["keywords"]:
            if keyword in user_message:
                return intent["response"]

    return (
        "Sorry, I couldn't understand your query. "
        "Please ask about packages, destinations, pricing, or booking process."
    )


