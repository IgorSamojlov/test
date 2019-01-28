from json import dumps
from json import loads

from db import msq

class Msg_worker():
    def __init__(self):
        self.m_sql = msq.Sql_worker()
        self.us_on = {}
        self.msg_in = None
        self.msg_out = None


    def read_msg(self, msg):
        try:
            self.msg_in = loads(msg)
        except Exception as e:
            if e:
                print('Error')
            self.fmsg_out('Error in messge from client')
            return

        if (self.msg_in['cmd'] == 'auth'):
            self.auth()

        elif (self.msg_in['cmd'] == 'reg'):
            print('Registraton \n')
            self.regis()

        elif (msg_in['cmd'] == 'get_user'):
            self.get_user_on()

        elif (self.msg_in['cmd'] == 'send_msg'):
            self.send_msg()

        elif (self.msg_in['cmd'] == 'quit'):
            self.us_quit(self.ws, self.msg_in['id'])

        elif (self. msg_in['cmd'] == 'get_message'):
            print ("get_message")

        elif (self. msg_in['cmd'] == 'message'):
            print(msg_in['msg'])


    def auth (self):
        if (self.m_sql.sql_auth(self.msg_in)):
            answ = True

            self.us_on[self.msg_in['login']] = 'ws'
            #self.sqlw.sql_us_on(self.msg_in, 'adr')
        else:
            answ = False
        self.fmsg_out({'cmd': 'auth', 'nick':'n', 'answer':answ})


    def get_user_on(self):
        us_on_t = list(set(self.get_key()) & set (self.msg_in['us']))
        self.fmsg_out({'cmd': 'us_on', 'us_on':us_on_t})


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

    def regis(self):
        print ('regis')
        if (self.m_sql.sql_regis(self.msg_in)):
            result = 'Done'
        else:
            result = 'Error'

        self.fmsg_out({'cmd':'reg', 'result':result})


    def fmsg_out(self, msg):
        self.msg_out = dumps(msg)
        print (self.msg_out)

