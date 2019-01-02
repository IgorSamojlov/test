import asyncio
import websockets
import json
import msq
import time

US = {}
US_ONLINE = {}
WS_OL = {}



async def get_user(ws):
    print ('Send user  ')
    us = list(US)
    nus = {}
    for i in us:
        nus[i] = US[i]['name']
    temp = json.dumps(nus)
    await ws.send(temp)

async def send_msg(ws, msg):
    if (msg['adr'] in US_ONLINE) and (US_ONLINE[msg['adr']]['ws'].open):
        m = (str(msg['mg']) + ' message from ' + str(msg['who']))
        await (US_ONLINE[msg['adr']]['ws'].send(m))

    if not (msg['adr'] in US_ONLINE):
        msq.add_message(msg['adr'], msg['ident'], msg['mg'],
         str(time.strftime('%X %x %Z')))

    if (msg['adr'] in US_ONLINE) and not(US_ONLINE[msg['adr']]['ws'].open):
        US_ONLINE.pop(msg['adr'])
        print ('adr ofline\n')
        print (US_ONLINE, 'online now\n')

async def auth(ws, msg):
    print ('auth')
    if ((msg['id'] in US) and (US[msg['id']]['pasw'] == msg['pasw'])):
        print ('Auth done..', str(ws.remote_address)  , '\n')
        US_ONLINE[msg['id']] = {'nick':US[msg['id']]['nick'], 'ws':ws}
        WS_OL[str(ws.remote_address)] = msg['id']

        print (US_ONLINE.values())
        await ws.send('True')
    else:
        await ws.send('False')

async def get_msg(ws, msg):
    temp = msq.get_message(msg['id'])
    t_msg = json.dumps(temp)
    await (ws.send(t_msg))

def ws_quit(ws, msg):
    US_ONLINE.pop(msg['id'])
    print (US_ONLINE, 'online now\n')

def abnor_quit(r_adr):
    US_ONLINE.pop(WS_OL[r_adr])
    print (US_ONLINE, 'online now\n')

async def echo(websocket, path):
    try:
        async for message in websocket:

            print ('Join: ')
            print(websocket.remote_address, '\n')
            print(message)
            msg = (json.loads(message))


            if (msg['cmd'] == 'auth'):
                await auth(websocket, msg)

            elif (msg['cmd'] == 'reg'):
                regis(websocket, msg)

            elif (msg['cmd'] == 'get_user'):
                await get_user(websocket)

            elif (msg['cmd'] == 'send_msg'):
                await send_msg(websocket, msg)

            elif (msg['cmd'] == 'quit'):
                ws_quit(websocket, msg)

            elif (msg['cmd'] == 'get_message'):
                await get_msg(websocket,msg)

    except Exception as e:
        print (e)
        print (e.code, websocket.remote_address)
        abnor_quit(str(websocket.remote_address))

        #await send_all(websocket)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
