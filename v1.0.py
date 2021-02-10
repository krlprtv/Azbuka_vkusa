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

stop = timeit.default_timer()
for i in range(15000):
    try:
        response = requests.get(urls['loc'][i], headers = headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        tovar_title.append(soup.find('h1').text)
        tovar_price.append(soup.find('div', class_="b-goods-price__sum b-price b-price_large js-price").find('b').text)
        tovar_category.append(soup.find('span', class_="b-product-menu__title").text)
        # Отловить неудачное соеднение
    except (AttributeError):
        tovar_price.append('No value')
    except (urllib3.exceptions.MaxRetryError):
        continue


df = pd.DataFrame(
    {'Title': tovar_title,
     'Price': tovar_price,
     'Category': tovar_category,
     },
    columns=['Title', 'Price', 'Category']
)
print(tovar_price)
df.to_excel(r'C:\Users\krlpr\Downloads\data15000.xlsx', index=False)

if (r/len(df)*100) < 5:
    expected_time = "Calculating..."
else:
    time_perc - timeit.default_timer()
    expected_time = np.round((time_perc - start) / (r/len(df)))/60, 2)
    
print("Current progress:", np.round(r/len(df)*100, 2), "%")
print("Current run time:", np.round(stop - start)/60, 2), "minutes")
print("Expected Run time:", expected_time, 'minutes')

-------------------------------------------------------------------
F:\Python\python.exe "F:/Python Projects/Parser/Pars.py"
Traceback (most recent call last):
  File "F:\Python\lib\site-packages\urllib3\connection.py", line 160, in _new_conn
    (self._dns_host, self.port), self.timeout, **extra_kw
  File "F:\Python\lib\site-packages\urllib3\util\connection.py", line 61, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "F:\Python\lib\socket.py", line 752, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:\Python\lib\site-packages\urllib3\connectionpool.py", line 677, in urlopen
    chunked=chunked,
  File "F:\Python\lib\site-packages\urllib3\connectionpool.py", line 381, in _make_request
    self._validate_conn(conn)
  File "F:\Python\lib\site-packages\urllib3\connectionpool.py", line 978, in _validate_conn
    conn.connect()
  File "F:\Python\lib\site-packages\urllib3\connection.py", line 309, in connect
    conn = self._new_conn()
  File "F:\Python\lib\site-packages\urllib3\connection.py", line 172, in _new_conn
    self, "Failed to establish a new connection: %s" % e
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPSConnection object at 0x000001D8F1376A88>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:\Python\lib\site-packages\requests\adapters.py", line 449, in send
    timeout=timeout
  File "F:\Python\lib\site-packages\urllib3\connectionpool.py", line 727, in urlopen
    method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]
  File "F:\Python\lib\site-packages\urllib3\util\retry.py", line 439, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='av.ru', port=443): Max retries exceeded with url: /i/332212/ (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001D8F1376A88>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Python Projects/Parser/Pars.py", line 20, in <module>
    response = requests.get(urls['loc'][i], headers = headers)
  File "F:\Python\lib\site-packages\requests\api.py", line 76, in get
    return request('get', url, params=params, **kwargs)
  File "F:\Python\lib\site-packages\requests\api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "F:\Python\lib\site-packages\requests\sessions.py", line 530, in request
    resp = self.send(prep, **send_kwargs)
  File "F:\Python\lib\site-packages\requests\sessions.py", line 643, in send
    r = adapter.send(request, **kwargs)
  File "F:\Python\lib\site-packages\requests\adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='av.ru', port=443): Max retries exceeded with url: /i/332212/ (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001D8F1376A88>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

Process finished with exit code 1

