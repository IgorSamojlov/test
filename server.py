import asyncio
import websockets
import json
import msq

async def echo(websocket, path):

    a = []

    print ('Hello')

    async for message in websocket:

        a.append(websocket)
        await websocket.send(message)
        print (a[0])

        msg = (json.loads(message))
        msq.add(msg)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8767))
asyncio.get_event_loop().run_forever()
