import os
import requests


def send_telegram(message: str):
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": chat_id,
            "text": message,
        },
        timeout=30,
    )
