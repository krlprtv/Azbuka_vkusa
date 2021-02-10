from typing import List
import timeit
import requests
import pandas as pd
from bs4 import BeautifulSoup, ResultSet

urls = pd.read_csv(r'C:\Users\krlpr\Downloads\urls.csv')
start = timeit.default_timer()
tovar_id = []
tovar_title = []
tovar_price = []
tovar_category = []

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/55.0.2883.87 Safari/537.36"}

for i in range(15000):
    try:
        response = requests.get(urls['loc'][i], headers = headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        tovar_title.append(soup.find('h1').text)
        tovar_price.append(soup.find('div', class_="b-goods-price__sum b-price b-price_large js-price").find('b').text)
        tovar_category.append(soup.find('span', class_="b-product-menu__title").text)
    except (AttributeError):
        tovar_price.append('No value')


df = pd.DataFrame(
    {'Title': tovar_title,
     'Price': tovar_price,
     'Category': tovar_category,
     },
    columns=['Title', 'Price', 'Category']
)
print(tovar_price)
df.to_excel(r'C:\Users\krlpr\Downloads\data15000.xlsx', index=False)
