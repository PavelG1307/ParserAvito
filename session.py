import requests

class Session():
    
    def __init__(self):
        self.headers_value = None
        self.session = requests.Session()
        self.count = 0
    
    def get(self, url, params):
        if self.count > 100:
            self.count = 0
            self.session = requests.Session()
            if self.headers:
                self.headers(self.headers_value)
        return requests.get(url=url, params=params, allow_redirects=True, timeout=5)
    
    def headers(self, headers):
        self.headers_value = headers
        self.session.headers.update(headers)
        
    def unquote(str):
        return requests.utils.unquote(str)