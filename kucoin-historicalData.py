import requests
from dotenv import load_dotenv
import os
import time
import base64
import hashlib
import hmac
import json
load_dotenv()
API_KEY_TESTING = os.getenv('API-KEY-TESTING')
API_SECRET_TESTING = os.getenv('API-SECRET-TESTING')
API_PASSPHRASE = os.getenv('API-PASSWORD')

api_key = API_KEY_TESTING
api_secret = API_SECRET_TESTING
api_passphrase = API_PASSPHRASE

months_to_go_back = 100  # Specify the number of months you want to go back
seconds_per_month = 2629746  # Number of seconds in one month
now = int(time.time() * 1000)
start_time = int(time.time() - (months_to_go_back * seconds_per_month))
start_time = str(start_time)
end_time = str(now)

url = f'https://api.kucoin.com/api/v1/market/candles?type=1day&symbol=BTC-USDT&startAt={start_time}&endAt={end_time}'
str_to_sign = str(now) + 'GET' + f'/api/v1/market/candles?type=1day&symbol=BTC-USDT&startAt={start_time}&endAt={end_time}'
signature = base64.b64encode(
    hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
passphrase = base64.b64encode(hmac.new(api_secret.encode('utf-8'), api_passphrase.encode('utf-8'), hashlib.sha256).digest())
headers = {
    "KC-API-SIGN": signature,
    "KC-API-TIMESTAMP": str(now),
    "KC-API-KEY": api_key,
    "KC-API-PASSPHRASE": passphrase,
    "KC-API-KEY-VERSION": "2"
}
response = requests.request('get', url, headers=headers)
jsonResponse = (json.loads(response.text))
data_size = (len(list(jsonResponse['data'])))

almostFormattedList = list(sublist[1:5] for sublist in jsonResponse['data'][0:1501]) # this gets the open close high and low in that order for the entire history from the api
formattedList = almostFormattedList[::-1] # this will reverse it so the last element is the latest 
print(formattedList)
