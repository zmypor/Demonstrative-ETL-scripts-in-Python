import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_bitcoin_data(days=365):
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        'vs_currency': 'usd',
        'days': days
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

bitcoin_data = get_bitcoin_data()



def parse_data(data):
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

bitcoin_df = parse_data(bitcoin_data)
print(bitcoin_df.describe())