from json import dumps
from json import loads

from db import msq

class Msg_worker():
    def __init__(self):
        self.m_sql = msq.Sql_worker()
        self.us_on = {}
        self.us_on_rev = {}
        self.msg_in = None
        self.msg_out = None
        self.ws = None
        self.ws_other = None
        self.msg_other = None

    def clear_other_msg(self):
        self.ws_other = None
        self.msg_other = None


    def read_msg(self, msg):
        try:
            self.msg_in = loads(msg)
        except Exception as e:
            if e:
                print('Error', e, self.msg_in)
                self.fmsg_out('Error in messge from client')
            return

        if (self.msg_in['cmd'] == 'auth') or (self.msg_in['cmd'] == 'reg'):
            if (self.msg_in['cmd']) == 'auth':
                self.auth()
            elif (self.msg_in['cmd'] == 'reg'):
                print('Registraton \n')
                self.regis()

        else:
            if (self.ws in self.us_on):
                print('User online ', self.us_on)

                if (self.msg_in['cmd'] == 'get_user'):
                    self.get_user_on()

                elif (self.msg_in['cmd'] == 'send_msg'):
                    self.send_msg()

                elif (self.msg_in['cmd'] == 'quit'):
                    self.us_quit(self.ws)

                elif (self.msg_in['cmd'] == 'get_message'):
                    print ("get_message")
                elif (self.msg_in['cmd'] == 'get_fr'):
                    self.get_fr()

                elif (self. msg_in['cmd'] == 'message'):
                    print(msg_in['msg'])
            else:
                print('User not online')

    def get_fr(self):
        friends = self.m_sql.sql_get_fr(self.us_on[self.ws])
        self.get_fr_on(friends)
        friends_on = self.get_fr_on(friends)
        self.fmsg_out({'cmd':'get_fr', 'friends':friends,
                        'fr_on':'ss', 'friends_on':list(friends_on)})


    def get_fr_on(self, user):
        set_user = set(self.us_on_rev.keys())
        return (set(user) & set_user)

    def auth (self):
        if (self.m_sql.sql_auth(self.msg_in)):
            answ = True

            self.us_on[self.ws] = self.msg_in['login']
            self.us_on_rev[self.msg_in['login']] = self.ws
            self.m_sql.sql_us_on(self.msg_in, str(self.ws.remote_address))
        else:
            answ = False
        self.fmsg_out({'cmd': 'auth', 'nick':'n', 'answer':answ})

    def send_msg(self):
        if (self.msg_in['adr'] in self.us_on_rev) and (
            self.us_on_rev[self.msg_in['adr']].open):
            print ('Send message: ')
            temp = {'cmd': 'msg',
                    'from':self.msg_in['from'],
                    'msg': self.msg_in['msg'],
                    'time': self.msg_in['time']}

            self.ws_other = self.us_on_rev[self.msg_in['adr']]

            self.msg_other = dumps(temp)
            self.fmsg_out({'cmd':'send_msg', 'res':'done'})


        elif (self.msg_in['adr'] not in self.us_on_rev) or not(
            self.us_on[self.msg_in['adr']].open):
            print('Message to que\n')
            self.m_sql.sql_add_message(self.msg_in)

        elif (self.msg_in['adr'] not in self.us_on):
            print('Error')
            #self.sqlw.msg_in_qu(self.msg_in)


    def msg_in_qu(self):
        self.sqlw.add_message(self.msg_in)

    def us_quit(self, ws):
        #self.sqlw.sql_us_on_del(ident)
        self.us_on.pop(self.ws)
        print (self.us_on)

    def regis(self):
        print ('regis')
        if (self.m_sql.sql_regis(self.msg_in)):
            result = 'Done'
        else:
            result = 'Error'

        self.fmsg_out({'cmd':'reg', 'answer':result})


    def fmsg_out(self, msg):
        self.msg_out = dumps(msg)
        print (self.msg_out)

    def abnorm_quit(self):
        if self.ws in self.us_on:
            self.us_on.pop(self.ws)
            self.us_on_rev.pop(self.us_on[self.ws])
        else:
            print('Abnorm_q error')
