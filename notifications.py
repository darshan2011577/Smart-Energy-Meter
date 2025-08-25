# alerts_telegram.py
import requests
def send_telegram(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    resp = requests.post(url, data={"chat_id":chat_id, "text":message})
    return resp.status_code==200

