import urllib.parse

def parse_request(data):
        try:
            data_p = data.split('\n')
            type = data_p[0].split(' ')[0]
            url = data_p[0].split(' ')[1]
            url = urllib.parse.unquote(url, encoding='utf-8', errors='replace')
            print(url)
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

        except Exception:
            return {
                'url': '',
                'type': '',
                'params': {},
                'endpoint': ''
            }


def get_response(data, code):
    if code == 500:
        response = f'HTTP/1.1 500 Internal Server Error\r\nContent-Type: application/json; charset=utf-8\r\n\r\n{data}'.encode('utf-8')
    elif code == 200:
        response = f'HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n{data}'.encode('utf-8')
    else:
        response = f'HTTP/1.1 400 Bad Request\r\nContent-Type: application/json; charset=utf-8\r\n\r\n{data}'.encode('utf-8')
    return response