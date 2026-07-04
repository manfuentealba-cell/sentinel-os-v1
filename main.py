import requests
import time

# CONFIGURACIÓN - LA LLENAMOS DESPUÉS
TELEGRAM_TOKEN = "TU_TOKEN_AQUI"
TELEGRAM_CHAT_ID = "TU_ID_AQUI"
PRECIO_ANTERIOR = 0

def obtener_precio_btc():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    return response.json()['bitcoin']['usd']

def enviar_alerta(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje}
    requests.post(url, data=data)

print("CENTINELA OS V0 INICIADO... Monitoreando BTC cada 5 min")

while True:
    try:
        precio_actual = obtener_precio_btc()
        cambio = ((precio_actual - PRECIO_ANTERIOR) / PRECIO_ANTERIOR) * 100 if PRECIO_ANTERIOR != 0 else 0
        
        print(f"Precio actual: ${precio_actual} | Cambio: {cambio:.2f}%")
        
        if PRECIO_ANTERIOR != 0 and abs(cambio) > 2: # Si sube o baja más de 2%
            enviar_alerta(f"🚨 ALERTA CENTINELA 🚨\nBTC: ${precio_actual}\nCambio: {cambio:.2f}%")
        
        PRECIO_ANTERIOR = precio_actual
        time.sleep(300) # Espera 5 minutos
    except:
        print("Error, reintentando en 60 seg...")
        time.sleep(60)
