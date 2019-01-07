import json
import asyncio
from json import dumps
from json import loads
import websockets
from db import msq
import os

class M_server():
    def __init__(self):
        print ('Heloo')
        self.us_on = {}
        self.msg_in = None
        self.msg_out = None
        self.ws = None
        self.ws_send = None
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
            answ = 'True'
            self.us_on[self.msg_in['id']] = self.ws
            self.sqlw.sql_us_on(self.msg_in, 'adr')#str(self.ws.remote_address))
        else:
            answ = 'False'
        self.msg_out = {'cmd': 'auth', 'answer':answ}

    def get_user_on(self):
        us_on_t = list(set(self.get_key()) & set (self.msg_in['us']))
        self.msg_out = {'cmd': 'us_on', 'us_on':us_on_t}

    def get_key(self):
        return self.us_on.keys()

    def send_msg(self):
        if (self.msg_in['adr'] in self.us_on) and (
            self.us_on[self.msg_in['adr']].open):
            print ('Send message: ')
            temp = {'cmd': 'msg', 'from':self.msg_in['from'],
             'msg': self.msg_in['msg'],
            'time': self.msg_in['time']}
            self.ws_send = self.us_on[self.msg_in['adr']]
            self.msg_out = temp

        elif (self.msg_in['adr'] in self.us_on) and not(
            self.us_on[self.msg_in['adr']].open):
            self.sqlw.msg_in_qu(self.msg_in)

        elif (self.msg_in['adr'] not in self.us_on):
            self.sqlw.msg_in_qu(self.msg_in)


    def msg_in_qu(self):
        self.sqlw.add_message(self.msg_in)

    def us_quit(self, ident):
        self.sqlw.sql_us_on_del(ident)
        self.us_on.pop(ident)

    def read_msg(self):
        if (self.msg_in['cmd'] == 'auth'):
            print ('Auth')
            self.auth()

        elif (self.msg_in['cmd'] == 'reg'):
            regis(websocket, msg)

        elif (self.msg_in['cmd'] == 'get_user'):
            self.get_user_on()

        elif (self.msg_in['cmd'] == 'send_msg'):
            self.send_msg()

        elif (self.msg_in['cmd'] == 'quit'):
            self.us_quit(self.ws, self.msg_in['id'])

        elif (self. msg_in['cmd'] == 'get_message'):
            pass


