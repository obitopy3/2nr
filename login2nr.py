import requests
import json

url = "https://api.2nr.xyz/auth/login"

payload = {
  "query": {
    "email": "email",
    "imei": "600a9c532c6c05e8",
    "language": "en",
    "password": "obito12##A"
  },
  "id": 101
}

headers = {
  'User-Agent': "okhttp/4.10.0",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json; charset=UTF-8",
  
}

response = requests.post(url, data=json.dumps(payload), headers=headers)
