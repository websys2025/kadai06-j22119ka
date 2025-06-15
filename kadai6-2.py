"""
参照したオープンデータ そらまめ君(環境省大気汚染物質広域監視システム)

エンドポイント https://soramame.env.go.jp/soramame/api/data_search

機能
観測データの検索
地域・測定局コードによる指定
年月範囲の指定

使用方法
GETリクエストを送信して、JSON形式でデータを取得。
パラメータに年月、都道府県、測定局、データ種別を設定。

"""


import requests
import pandas as pd
import json

url = "https://soramame.env.go.jp/soramame/api/data_search"

params = {
    "Start_YM": "202504", #開始年度
    "End_YM": "202505", #終了年度
    "TDFKN_CD": "08", #都道府県の設定(茨城県)
    "SKT_CD": "08406050", #詳しい地点(地点は神栖消防)
    "REQUEST_DATA": "TEMP", #ほしいデータ(例 気温)
    "lang": "J",  # 日本語を指定
}

response = requests.get(url, params=params)

data = response.json()

print(data)
