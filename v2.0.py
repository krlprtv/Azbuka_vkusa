from typing import List
import tqdm
import requests
import pandas as pd
from bs4 import BeautifulSoup, ResultSet
from multiprocessing import Pool

urls = pd.read_csv(r'C:\Users\krlpr\Downloads\urls.csv')
urls_list = urls['loc'].to_list()

tovar_id = []
tovar_title = []
tovar_price = []
tovar_category = []
links = []
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/55.0.2883.87 Safari/537.36"}
def parse(urls):
    for i in tqdm.tgrange(100):
        try:
            response = requests.get(urls_list[i], headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                tovar_title.append(soup.find('h1',class_="b-goods__title js-goods-title").text)
                tovar_price.append(soup.find('div', class_="b-goods-price__sum b-price b-price_large js-price").find('b').text)
                tovar_category.append(soup.find('span', class_="b-link b-link_underline").text)
                links.append(urls_list[i])
            # Отловить неудачное соеднение itemprop='name
            else:
                continue
        except (AttributeError):
            tovar_price.append('No value')
            tovar_category.append('No value')
        except (urllib3.exceptions.MaxRetryError):
            continue
        
p = Pool(10)
p.map(parse, urls_list)

df = pd.DataFrame(
    {'Title': tovar_title,
     'Price': tovar_price,
     'Category': tovar_category,
     'Link':links
     },
    columns=['Title', 'Price', 'Category','Link']
)

df.to_excel(r'F:\Python Projects\Parser\data100_3.xlsx', index=False)
