import requests
import pandas as pd
import json

url = "https://soramame.env.go.jp/soramame/api/data_search"

params = {
    "Start_YM": "202504", 
    "End_YM": "202505",
    "TDFKN_CD": "08",
    "SKT_CD": "08406050",
    "REQUEST_DATA": "TEMP", 
    "lang": "J",  # 日本語を指定
}

response = requests.get(url, params=params)

data = response.json()

print(data)
