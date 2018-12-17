import asyncio
import websockets
import json

async def test():

    async with websockets.connect('ws://127.0.0.1:8767') as websocket:

        name = ''

        while name != 'quit':

            name = input('You name ')
            surname = input('Surname ')
            adr = input('Adres ')
            msg = [name, surname, adr]
            mes = json.dumps(msg)

            await websocket.send(mes)

            response = await websocket.recv()
            print(response)

asyncio.get_event_loop().run_until_complete(test())
