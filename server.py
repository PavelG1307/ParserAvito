from logging import exception
from pydoc import pager
import socket
import urllib.parse

class Server():

    def __init__(self, host='127.0.0.1', port=8080):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(4)
        print('Server working...')

    def parse_rec(self, data):
        data_p = data.split('\n')
        type = data_p[0].split(' ')[0]
        url = data_p[0].split(' ')[1]
        params={}
        endpoint = url.split('?')[0]
        if len(url.split('?')) > 1:
            parametrs = url.split('?')[1].split('&')
            for p in parametrs:
                key, value = p.split('=')
                params[key] = value
        
        return {
            'url': url,
            'type': type,
            'params': params,
            'endpoint': endpoint
        }
