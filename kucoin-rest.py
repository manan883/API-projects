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
url = 'https://api-futures.kucoin.com/api/v1/contracts/active'
now = int(time.time() * 1000)
str_to_sign = str(now) + 'GET' + '/api/v1/contracts/active'
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
# print(response.status_code)
# print(response.json())
# temp = response.json()
jsonResponse = json.loads(response.text)
totalContracts = len(list(jsonResponse['data'])) - 1
maxFundingRateSymbol = ""
for i in range(totalContracts):
    exit

print(totalContracts)
print(jsonResponse['data'][totalContracts]['fundingFeeRate'])

