import socket
import asyncio
from threading import Thread
import uuid
from helpers import parse_request, get_response

class Server():

    def __init__(self, host='127.0.0.1', port=8080):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(4)
    

    async def handle_get_endpoints(self, endpoint, params, inspector, parser_user, parser_region):
        try:
            if endpoint == '/api/parse/user':
                if not inspector.check_user(params["user"]):
                    parser_uuid = str(uuid.uuid4())
                    Thread(target=parser_user,args = (params["user"],params["owner_uuid"], inspector,parser_uuid)).start()
                    await asyncio.sleep(0.25)
                    if inspector.check_uuid(parser_uuid) and not inspector.check_error(parser_uuid):
                        return {'res': {"status": "ok", 'parser_uuid': parser_uuid}, 'code': 200}
                    else:
                        return {'res': {"status": "Bad Request"}, 'code': 400}
                else:
                    return {'res': {"status": "Bad Request"}, 'code': 400}


            elif endpoint == '/api/parse/check':
                parser_uuid = params["uuid"]
                if inspector.check_uuid(parser_uuid):
                    res = {"status": "In progress"}
                    code = 200
                    
                elif not inspector.check_error(parser_uuid):
                    result = inspector.getResult(parser_uuid)
                    res = {"status": "Done", "result": result}
                    code = 200
                return {'res': res, 'code': code}


            elif endpoint == '/api/parse/region':
                parser_uuid = str(uuid.uuid4())
                print(parser_uuid)
                if 'categoryId' in params.keys():
                    categoryId = params["categoryId"]
                else:
                    categoryId = 42
                if 'locationId' in params.keys():
                    locationId = params["locationId"]
                else:
                    locationId = 621540
                Thread(target = parser_region,
                        args = ( 
                            inspector, 
                            params["search"], 
                            params["owner_uuid"],
                            categoryId,
                            locationId,
                            parser_uuid
                        )).start()
                await asyncio.sleep(0.5)
                if inspector.check_uuid(parser_uuid) and not inspector.check_error(parser_uuid):
                    return {'res': {"status": "ok", 'parser_uuid': parser_uuid}, 'code': 200}
                else:
                    return {'res': {"status": "Bad Request"}, 'code': 400}
                    
            else: 
                return {'res': {'status': 'Bad request'}, 'code': 400}
 
        except Exception as e:
            print(e)
            return {'res': {"status": "Bad request"}, 'code': 400}


    async def handl(self, inspector, parser_user, parser_region):
        client_socket, address = self.server.accept()
        data = client_socket.recv(1024).decode('utf-8')
        data_p = parse_request(data)

        if data_p['type'] == 'GET':
            data_r = await self.handle_get_endpoints(data_p['endpoint'], data_p['params'], inspector, parser_user, parser_region)
            print(data_r)
            response = get_response(data_r['res'], data_r['code'])
            client_socket.send(response)
