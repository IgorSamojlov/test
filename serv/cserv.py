import json
from serv import msgworker

msg_serv = msgworker.Msg_worker()

async def run(websocket, path):

    print ('Join: ')
    print(websocket.remote_address, ' ')

    await websocket.send(json.dumps({'cmd':'msg',
     'text':'Hello from server', 'name':'Server'}))


    try:
        async for message in websocket:
            print(message)
            msg_serv.read_msg(message)
            print (msg_serv.msg_out)
            await (websocket.send(msg_serv.msg_out))

    except Exception as e:
        pass
