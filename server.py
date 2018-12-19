import asyncio
import websockets
import json
import msq

US = {}

def regis(ws, msg):

    US[msg['autn']] = {'name': msg['name'], 'pasw':msg['pasw'],
    'nick': msg['nick'], 'ws':ws}

    print ('All who conn \n')
    print(US)
    print ('\n')

async def send_all(ws):
    auth = list(US)
    for au in auth:
        if (US[au]['ws'].open):
            await US[au]['ws'].send('You are here?\n')

async def echo(websocket, path):
    async for message in websocket:

        print ('Join \n')
        print(websocket.remote_address, '\n')

        msg = (json.loads(message))
        regis(websocket, msg)
        await send_all(websocket)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
