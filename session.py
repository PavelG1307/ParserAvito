from email import header
import json
import time
import requests
from requests.utils import unquote
import urllib.parse

class Session():
    

    def __init__(self, timeout = 2):
        self.headers_v = {}
        self.timeout = timeout
        self.session = requests.Session
        self.headers_v = {
                    'authority': 'm.avito.ru',
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'none',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'accept-language': 'ru-RU,ru;q=0.9'
                    }
        self.headers(self.headers_v)
        resp = requests.get(url = 'https://m.avito.ru', allow_redirects=True)
        if resp.status_code == 403:
            time.sleep(1)
            requests.get(url = 'https://m.avito.ru/#block', allow_redirects=True)
        time.sleep(1)


    def restart(self):
        self.session = requests.Session
        self.headers(self.headers_v)
        resp = requests.get(url = 'https://m.avito.ru', allow_redirects=True)
        if resp.status_code == 403:
            time.sleep(1)
            requests.get(url = 'https://m.avito.ru/#block', allow_redirects=True)
        time.sleep(2)


    def get(self, url, params):
        resp = requests.get(url=url, params=params, allow_redirects=True)
        time.sleep(4)
        if resp.status_code == 403:
            print('FORBIDDEN!')
            resp = requests.get(url = 'https://m.avito.ru', allow_redirects=True)
            if resp.status_code == 403:
                time.sleep(1)
                requests.get(url = 'https://m.avito.ru/#block', allow_redirects=True)
            time.sleep(2)
            resp = requests.get(url=url, params=params, allow_redirects=True)
            if resp.status_code == 403:
                print('FORBIDDEN! RESTART SESSION!')
                self.restart()
                return self.get(url, params)
        return resp.json()
    
   
        

    def headers(self, headers):
        self.headers_v = headers
        self.session.headers = headers
        
    def unquote(self, str):
        return unquote(str)