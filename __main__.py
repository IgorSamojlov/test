import websockets
from serv import cserv
import asyncio

def main():
    sserv = cserv.M_server()

    asyncio.get_event_loop().run_until_complete(
        websockets.serve(sserv.run, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    main()
