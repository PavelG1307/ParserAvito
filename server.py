import socket
from unicodedata import category
import urllib.parse
import asyncio
from threading import Thread

class Server():

    def __init__(self, host='127.0.0.1', port=8080):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(4)
        print('Server working...')


    def parse_rec(self, data):
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
    

    async def handle_get_endpoints(self, endpoint, params, parser, inspector, callback, callback_all):
        try:
            print(endpoint)
            if endpoint == '/api/parse':
                if not inspector.check_user_in_parsing(params["user"]):
                    print(f'Parsing user {params["user"]}')
                    Thread(target=callback, args = (params["user"],params["owner_uuid"],parser,inspector,)).start()
                    await asyncio.sleep(0.5)
                    if inspector.check_user_in_parsing(params["user"]) and not inspector.check_user_in_error(params["user"]):
                        return {'res': {"status": "ok"}, 'code': 200}
                    else:
                        return {'res': {"status": "Bad Request"}, 'code': 400}
                else:
                    return {'res': {"status": "Bad Request"}, 'code': 400}


            elif endpoint == '/api/parse/check':
                if inspector.check_user_in_parsing(params["user"]):
                    res = {"status": "In progress"}
                    code = 200
                elif not inspector.check_user_in_error(params["user"]):
                    result = inspector.getResult(params["user"])
                    res = {"status": "Done", "result": result}
                    code = 200
                else:
                    print('Internal error')
                    res = {"status": "Bad request"}
                    code = 400
                return {'res': res, 'code': code}
            

            elif endpoint == '/api/parse/all':
                    if not inspector.check_user_in_parsing(params["owner_uuid"]):
                        if 'categoryId' in params.keys():
                            categoryId = params["categoryId"]
                        else:
                            categoryId = 42
                        if 'locationId' in params.keys():
                            locationId = params["locationId"]
                        else:
                            locationId = 621540
                        Thread(target = callback_all,
                                args = (
                                    parser, 
                                    inspector, 
                                    params["search"], 
                                    params["owner_uuid"],
                                    categoryId,
                                    locationId
                                )).start()
                        await asyncio.sleep(0.5)
                        if inspector.check_user_in_parsing(params["owner_uuid"]) and not inspector.check_user_in_error(params["owner_uuid"]):
                            return {'res': {"status": "ok"}, 'code': 200}
                        else:
                            return {'res': {"status": "Bad Request"}, 'code': 400}
                    else:
                        return {'res': {'status': 'Bad request'}, 'code': 400}
                    

            elif endpoint == '/api/parse/check/all':
                if inspector.check_user_in_parsing(params["owner_uuid"]):
                    res = {"status": "In progress"}
                    code = 200

                elif not inspector.check_user_in_error(params["owner_uuid"]):
                    result = inspector.getResult(params["owner_uuid"])
                    res = {"status": "Done", "result": result}
                    code = 200
                else:
                    print('Internal error')
                    res = {"status": "Bad request"}
                    code = 500
                return {'res': res, 'code': code}

            else: 
                return {'res': {'status': 'Bad request'}, 'code': 400}
 
        except Exception as e:
            print(e)
            return {'res': {"status": "Bad request"}, 'code': 400}


    async def handl(self, parser, inspector, callback, callback_all):
        client_socket, address = self.server.accept()
        data = client_socket.recv(1024).decode('utf-8')
        data_p = self.parse_rec(data)
        if data_p['type'] == 'GET':
            r = await self.handle_get_endpoints(data_p['endpoint'], data_p['params'], parser, inspector, callback, callback_all)
            if r['code'] == 500:
                answ = f'HTTP/1.1 500 Internal Server Error\r\nContent-Type: application/json; charset=utf-8\r\n\r\n{r["res"]}'.encode('utf-8')
            elif r['code'] == 400:
                answ = f'HTTP/1.1 400 Bad Request\r\nContent-Type: application/json; charset=utf-8\r\n\r\n{r["res"]}'.encode('utf-8')
            else:
                answ = f'HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n{r["res"]}'.encode('utf-8')
            client_socket.send(answ)
