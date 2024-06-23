import requests
import time

def get_bitcoin_data():
    try:
        response = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD")
        data = response.json()
        return data.get('USD')
    except Exception as e:
        print("Error fetching Bitcoin data:", e)
        return None

def calculate_average(bitcoin_values):
    if not bitcoin_values:
        return None
    return sum(bitcoin_values) / len(bitcoin_values)

if __name__ == "__main__":
    bitcoin_values = []
    while True:
        bitcoin_price = get_bitcoin_data()
        if bitcoin_price:
            bitcoin_values.append(bitcoin_price)
            if len(bitcoin_values) > 60:  # Keep only the last 10 minutes (60 * 10 sec = 600 sec)
                bitcoin_values = bitcoin_values[-60:]
            average_price = calculate_average(bitcoin_values)
            print("Current Bitcoin price:", bitcoin_price, "USD")
            print("Average price over the last 10 minutes:", average_price, "USD")
        time.sleep(10)  # Fetch data every 10 seconds
