import asyncio
import websockets
import json
import time

async def test():

    async with websockets.connect('ws://127.0.0.1:8765') as websocket:

        msg = {'autn': str(time.time()),
        'name': 'Igor', 'pasw':'1111','nick':'Igor_sam'}
        mes = json.dumps(msg)

        await websocket.send(mes)

        response = await websocket.recv()
        print(response)
        websocket.close()

asyncio.get_event_loop().run_until_complete(test())
