import requests
import urllib


def get_api(url):
    min_price=[]
    max_price=[]
    product_name=[]
    r = requests.get(url)
    products=r.json()["Products"]
    for p in products:
        product = p["Product"]
        product_name.append(product["productName"])
        min_price.append(product["minPrice"])
        max_price.append(product["maxPrice"])
    word=input("商品名を入力してください:")
    for name,min,max in zip(product_name,min_price,max_price):
        if word in name:
            print(f"{name}の最安値は{min}円、最高値は{max}円です")
        


def main():
    keyword = input("検索キーワードを入力して下さい：")
    url = f"https://app.rakuten.co.jp/services/api/Product/Search/20170426?format=json&keyword={keyword}&applicationId=1019079537947262807"
    get_api(url)


main()
