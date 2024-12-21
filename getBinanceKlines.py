import requests
import pandas as pd


def get_binance_klines(symbol='BTCUSDT', interval='1m', limit=1000):
    """
    Obtain historical candlestick data for Binance trading pairs.

   Parameters:
  -Symbol: Trading pair (e.g. BTCUSDT)
  -Interval: time interval (e.g. '1m', '5m', '1h', '1d')
  -Limit: Limit on the number of returned data (up to 1000)

  return:
  -The DataFrame contains time, opening price, highest price, lowest price, closing price, and trading volume.
    """
    url = "https://api.binance.com/api/v3/klines"
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Creating DataFrame
    columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time',
               'Quote Asset Volume', 'Number of Trades', 'Taker Buy Base Volume',
               'Taker Buy Quote Volume', 'Ignore']
    df = pd.DataFrame(data, columns=columns)

    # Converting timestamp
    df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms')
    df['Close Time'] = pd.to_datetime(df['Close Time'], unit='ms')

    return df


# Return simplified fields
# return df[['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume']]

# Usage example
df_binance = get_binance_klines(symbol='BTCUSDT', interval='1m', limit=1000)
# Saved as local .csv file for later re-test
df_binance.to_csv('BTCUSDT.csv')
print(df_binance.head())