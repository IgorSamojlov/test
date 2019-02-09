import websockets
from serv import cserv

import asyncio

def main():

    asyncio.get_event_loop().run_until_complete(
        websockets.serve(cserv.run, 'localhost', 5000))
    asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    main()
