from typing import List

import requests
import pandas as pd
from bs4 import BeautifulSoup, ResultSet

urls = pd.read_csv(r'C:\Users\krlpr\Downloads\urls.csv')

tovar_id = []
tovar_title = []
tovar_price = []
tovar_category = []

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/55.0.2883.87 Safari/537.36"}

for i in len(urls.shape[0]):
    response = requests.get(urls['loc'][i], headers = headers)
    # Можно попробовать занметь html на lxml
    soup = BeautifulSoup(response.text, 'html.parser')
    tovar_title.append(soup.find('h1').text)
    tovar_price.append(soup.find('div', class_="b-goods-price__sum b-price b-price_large js-price").text)
    tovar_category.append(soup.find('span', class_="b-product-menu__title").text)

# Попробовать такой подход
# tovar_ids_ = soup.find_all('div, class_"b-goods-price__sum b-price b-price_large js-price")
# Или
# tovar_ids = soup.find('div', {'class':'b-goods-price__sum b-price b-price_large js-price'}).find('b') Добавить find('b') в 23 строку



df = pd.DataFrame(
    {'Title': tovar_title,
     'Price': tovar_price,
     'Category': tovar_category,
     },
    columns=['Title', 'Price', 'Category']
)

df.to_excel(r'C:\Users\krlpr\Downloads\urls100.xlsx', index=False)
