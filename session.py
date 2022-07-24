import json
import time
import requests
from requests.utils import unquote
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class Session():
    

    def __init__(self, timeout = 2):
        self.timeout = timeout
        self.options = Options()
        self.options.set_preference('devtools.jsonview.enabled', False)
        self.options.headless = True
        self.options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.get('https://m.avito.ru')
        time.sleep(3)


    def restart(self):
        self.driver.close()
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.get('https://m.avito.ru')
        time.sleep(3)


            

    def get(self, url, params):
        try:
            if params:
                url = url + '?' + urllib.parse.urlencode(params)
            self.driver.get(url)
            time.sleep(2)
            content = self.driver.page_source
            source = BeautifulSoup(content, 'lxml').find("pre").text
            req = json.loads(source)
            if 'status' in req.keys():
                if req['status'] == 'forbidden':
                    print(req)
                    self.driver.get('https://m.avito.ru')
                    time.sleep(3)
                    self.driver.get(url)
                    content = self.driver.page_source
                    source = BeautifulSoup(content, 'lxml').find("pre").text
                    req = json.loads(source)
                    if 'status' in req.keys():
                        if req['status'] == 'forbidden':
                            print(req)
                            self.restart()
                            return self.get(url, None)
            return req
        except Exception as e:
            print(e)
            self.restart()
            return self.get(url, None)
    
   
        

    def headers(self, headers):
        pass
        
    def unquote(self, str):
        return unquote(str)