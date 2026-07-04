import requests
import time

TOKEN = "7957149676:AAH1HGe1CPwxCJ8d98zZUa6-fokNpz5ZPDI"
CHAT_ID = "5630322088"

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensaje}
    requests.post(url, data=data)

# PRUEBA: Alerta de que el bot está vivo
enviar_telegram("🚨 CENTINELA OS V1 ACTIVO 🚨\n\nEstoy vigilando el mercado 24/7 CEO")

print("Bot enviado. Revisa tu Telegram.")
