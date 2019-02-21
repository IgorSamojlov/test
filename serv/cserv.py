import json
from serv import msgworker
import asyncio

msg_serv = msgworker.Msg_worker()

async def run(websocket, path):

    print ('Join: ')
    print(websocket.remote_address, ' ')

    await websocket.send(json.dumps({'cmd':'msg',
     'msg':'Hello from server', 'from':'Server'}))
    try:
        async for message in websocket:
            print(message)
            msg_serv.ws = websocket
            msg_serv.read_msg(message)

            try:
                await websocket.send(msg_serv.msg_out)
                if msg_serv.msg_other:
                    await msg_serv.ws_other.send(msg_serv.msg_other)
                    msg_serv.clear()

            except Exception as e:
                print(e)

    except Exception as e:
        #if (e.code == 1006):
            msg_serv.ws = websocket
            msg_serv.abnorm_quit()
