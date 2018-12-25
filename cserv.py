import json
import asyncio
import websockets
import msq

class Ck():
    def __init__(self):
        print ('Heloo')
        self.msg = None
        self.ws = None
        self.sqlw = msq.Sql_worker('new.db')

    async def c(self, websocket, path):
        try:
            async for message in websocket:

                print ('Join: ')
                print(websocket.remote_address, '\n')
                print(message)
                self.msg = (json.loads(message))
                self.ws = websocket
                await self.read_msg()

        except Exception as e:

            print (e)
            print (e.code, websocket.remote_address)
            abnor_quit(str(websocket.remote_address))

    async def auth (self):
        if (self.sqlw.sql_auth(self.msg['ident'], self.msg['pasw'])):
            await (self.ws.send('True'))
        else:
            await (self.ws.send('False'))


    async def read_msg(self):
        if (self.msg['cmd'] == 'auth'):
            await self.auth()

        elif (self.msg['cmd'] == 'reg'):
            regis(websocket, msg)

        elif (self.msg['cmd'] == 'get_user'):
            pass

        elif (self.msg['cmd'] == 'send_msg'):
            pass

        elif (self.msg['cmd'] == 'quit'):
            ws_quit(websocket, msg)

        elif (self. msg['cmd'] == 'get_message'):
            pass



a = Ck()

asyncio.get_event_loop().run_until_complete(
    websockets.serve(a.c, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
