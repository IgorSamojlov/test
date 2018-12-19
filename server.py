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
            print ('open')
            await US[au]['ws'].send('Hello evere one\n')

async def get_user(ws):
    print ('Send user  ')
    us = list(US)
    print(us)
    await ws.send(us)


async def send_msg(ws, msg):
    if (US[msg['adr']]['ws'].open):
        m = (str(msg['mg']) + ' message from ' + str(msg['who']))
        if (US[msg['adr']]['ws'].open):

            await (US[msg['adr']]['ws'].send(m))

        elif (not US[msg['adr']]['ws'].open):
            print('offline\n')

async def echo(websocket, path):
    async for message in websocket:

        print ('Join \n')
        print(websocket.remote_address, '\n')
        msg = (json.loads(message))

        if (msg['cmd'] == 'reg'):
            regis(websocket, msg)
        elif (msg['cmd'] == 'get_user'):
            await get_user(websocket)

        elif (msg['cmd'] == 'send_msg'):
            await send_msg(websocket, msg)

        #await send_all(websocket)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
