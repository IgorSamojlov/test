import asyncio
import websockets
import json
import time
import threading


WB = []


async def reg(ws):
    msg = {'cmd': 'reg', 'autn': str(time.time()),
        'name': 'Igor', 'pasw':'1111','nick':'Igor_sam'}
    mes = json.dumps(msg)

    await ws.send(mes)

async def get_user(ws):
    msg = {'cmd': 'get_user'}
    mes = json.dumps(msg)
    await ws.send(mes)
    m = (await ws.recv())
    d = json.loads(m)
    print (d)

async def send_msg(ws, ident):
    mg = input('Enter message.... ')
    adr = input('Address.... ')
    msg = {'cmd':'send_msg', 'who':'Igor', 'mg':mg, 'adr':adr, 'ident': ident}
    temp = json.dumps(msg)
    await ws.send(temp)

async def auth(iden, pasw, ws):
    msg = {'cmd':'auth','id':iden,'pasw':pasw}
    temp = json.dumps(msg)
    await ws.send(temp)
    return (await (ws.recv()))

async def quit(ws, ident):
    msg = {'cmd':'quit', 'id': ident}
    temp = json.dumps(msg)
    await ws.send(temp)

async def get_message(ws, ident):
    msg = {'cmd':'get_message', 'id':ident}
    temp = json.dumps(msg)
    await ws.send(temp)
    temp = await (ws.recv())
    t = json.loads(temp)
    print ('You have ', len(t), ' messages')
    for m in t:
        print ('Message from ', m[1], ' ', m[2], ' ', m[3])

async def test(ident, pasw):

    async with websockets.connect('ws://127.0.0.1:8765') as websocket:


        thread = threading.Thread(target=reciving, args=(websocket,))
        thread.start()

        if (await auth(ident, pasw, websocket) == 'True'):
            print('Auth done')
            await (get_message(websocket, ident))

            while True:
                cmd = input ('__ ')
                if cmd == 'reg':
                    await reg(websocket)

                elif cmd == 'get_user':
                    await get_user(websocket)

                elif cmd == 'send_msg':
                    await send_msg(websocket, ident)

                elif cmd == 'get_m':
                    get_message()

                elif cmd == 'get':
                    temp = await websocket.recv()
                    print (temp)
                elif cmd == 'quit':
                    await quit(websocket, ident)
                    break
        else:
            print('Auth error, try again\n')

        #response = await websocket.recv()
        #print(response)
        websocket.close()
        thread.join()

ident = '972f46723b38495f94d1d337f52e6f25'
asyncio.get_event_loop().run_until_complete(test(ident, '22222'))
