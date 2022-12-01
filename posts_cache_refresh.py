import requests
import time
import threading

url_root = 'http://172.23.245.127:8085/post/page/'
cached_page_nums = [1, 2, 3, 4]

headers = {
    "content-type": "application/json;charset=UTF-8",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42',
}

def refresh_thread():
    while True:
        for page_num in cached_page_nums:
            url = f"{url_root}{page_num}"
            requests.get(url, headers=headers)
            print('refreshed page: ', url)
            time.sleep(1)

for i in range(1):
    t = threading.Thread(target=refresh_thread)
    t.daemon = True
    t.start()
    time.sleep(3)

while True:
    time.sleep(1)