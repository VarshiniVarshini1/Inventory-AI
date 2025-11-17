import requests
import config

def send_whatsapp(number, message):
    payload = {
        "apikey": config.WHATSAPP_API,
        "number": number,
        "message": message
    }
    
    res = requests.post("https://your-whatsapp-api.com/send", json=payload)
    return res.json()
