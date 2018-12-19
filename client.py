import asyncio
import websockets
import json
import time


async def reg(ws):
    msg = {'cmd': 'reg', 'autn': str(time.time()),
        'name': 'Igor', 'pasw':'1111','nick':'Igor_sam'}
    mes = json.dumps(msg)

    await ws.send(mes)

async def get_user(ws):
    msg = {'cmd': 'get_user', 'autn': str(time.time()),
        'name': 'Igor', 'pasw':'1111','nick':'Igor_sam'}
    mes = json.dumps(msg)
    await ws.send(mes)
    mes = await ws.recv()
    print (mes)

async def send_msg(ws, mg, adr):
    msg = {'cmd':'send_msg', 'who':'Igor', 'mg':mg, 'adr':adr}
    ms = json.dumps(msg)
    await ws.send(ms)

async def test():

    async with websockets.connect('ws://127.0.0.1:8765') as websocket:


        while True:
            cmd = input ('__ ')
            if cmd == 'reg':
                await reg(websocket)

            elif cmd == 'get_user':
                await get_user(websocket)

            elif cmd == 'send_msg':
                ad = input('Adress__ ')
                ms = input ('Messge__ ')
                await send_msg(websocket, ms, ad)

            elif cmd == 'get':
                a = await websocket.recv()
                print (a)
            elif cmd == 'quit':

                break

        #response = await websocket.recv()
        #print(response)


        websocket.close()

asyncio.get_event_loop().run_until_complete(test())
