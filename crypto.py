import requests
import matplotlib.pyplot as plt
from datetime import datetime  
import csv

def get_crypto_price(coin_id="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[coin_id]["usd"]
    else:
        print("Error al llamar a la API")
        return None

def get_historical_data(coin_id="bitcoin", days=30):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days={days}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        prices = [entry[1] for entry in data["prices"]]
        dates = [entry[0] for entry in data["prices"]]
        return dates, prices
    else:
        print("Error al obtener datos históricos")
        return None

def save_to_csv(coin_id="bitcoin", days=30):
    dates, prices = get_historical_data(coin_id, days)
    with open(f"{coin_id}_prices.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Fecha", "Precio (USD)"])
        for date, price in zip(dates, prices):
            formatted_date = datetime.fromtimestamp(date/1000).strftime("%Y-%m-%d")  # <-- Usa datetime directamente
            writer.writerow([formatted_date, price])
    print(f"Datos guardados en {coin_id}_prices.csv")

if __name__ == "__main__":
    save_to_csv("ethereum", 7)  # Ejemplo de uso