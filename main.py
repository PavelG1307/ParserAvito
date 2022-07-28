from parser import Parser
from inspector import Inspector
from server import Server
import asyncio

def main():
    try:
        parser = Parser()
        parser.connectDB(dbname='default', user='master', password='6sd1v838', host='194.177.21.255')

        inspector = Inspector()

        serv = Server(port = 8081)

        while(True):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(serv.handl(inspector, parser.parse_user, parser.parse_region))

    except KeyboardInterrupt:
        serv.server.close()
        print('\nGoodBye')


if __name__ == '__main__':
        main()
