import requests
import urllib
import pandas as pd


def get_api(url):
    item_rank=[]
    item_name=[]
    item_price=[]
    r = requests.get(url)
    items=r.json()["Items"]
    for i in items:
        item=i["Item"]
        item_rank.append(item["rank"])
        item_name.append(item["itemName"])
        item_price.append(item["itemPrice"])
    df = pd.DataFrame({"順位":item_rank,"商品名":item_name,"値段":item_price})
    df.to_csv("ranking.csv", encoding = "utf-8-sig")
        

def main():
    genre_id = input("ジャンルIDを入力して下さい：")
    url = f"https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?format=json&genreId={genre_id}&applicationId=1019079537947262807"
    get_api(url)


main()
