import json
import asyncio
from json import dumps
from json import loads
import websockets
from db import msq

class M_server():
    def __init__(self):
        print ('Heloo')
        self.us_on = {}
        self.msg_in = None
        self.msg_out = None
        self.ws = None
        self.sqlw = msq.Sql_worker()

    async def run(self, websocket, path):
        try:
            async for message in websocket:

                print ('Join: ')
                print(websocket.remote_address, '\n')
                self.msg = (loads(message))
                self.ws = websocket
                self.read_msg()
                if self.msg_out != None:
                    temp = json.dumps(self.msg_out['msg'])
                    try:
                        self.ws.send(temp)
                        self.msg_out = None
                    finally:
                        msg_in_qu(self.msg_in)
        except Exception as e:

            print (e)
            print (e.code, websocket.remote_address)
            abnor_quit(str(websocket.remote_address))

    def auth (self):
        if (self.sqlw.sql_auth(self.msg_in)):
            self.msg_out = 'True'
            print ('True')
            self.us_on[self.msg_in['id']] = self.ws
            self.sqlw.sql_us_on(self.msg_in, 'adr')#str(self.ws.remote_address))
        else:
            self.msg_out = 'False'

    def send_msg(self):
        if (self.msg_in['adr'] in self.us_on) and (
            self.us_on[msg_in['adr']].ws.open):
            print ('Send message: ')
            self.msg_out = self.msg_in['msg']
        else:
            self.sqlw.msg_in_qu(self.msg_in)
            ws = self.user_on[msg_in['adr']]
            self.us_quit(ws, msg_in['adr'])

    def msg_in_qu(self):
        self.sqlw.add_message(self.msg_in)

    def us_quit(self, ws, ident):
        self.sqlw.sql_us_on_del(ident)
        if self.us_on:
            self.us_on.pop(ident)

    def read_msg(self):
        if (self.msg_in['cmd'] == 'auth'):
            print ('Auth')
            self.auth()

        elif (self.msg_in['cmd'] == 'reg'):
            regis(websocket, msg)

        elif (self.msg_in['cmd'] == 'get_user'):
            pass

        elif (self.msg_in['cmd'] == 'send_msg'):
            pass

        elif (self.msg_in['cmd'] == 'quit'):
            self.us_quit(self.ws, self.msg_in['id'])

        elif (self. msg_in['cmd'] == 'get_message'):
            pass

