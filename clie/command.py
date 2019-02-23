from json import load
from json import dumps

class Mcmd():
    def __init__(self):
        self.cmd = None
        self.msg_out = None

    def read_msg(self, cmd):
        print('reaaad')
        if (cmd == 'auth'):
            self.auth()
        elif (cmd == 'reg'):
            self.regis()
        elif (cmd == 'get_fr'):
            self.get_fr()
        elif (cmd == 'q'):
            self.quit_m()
        elif (cmd == 'send_msg'):
            self.send_msg()

    def f_msg(self, msg):
        self.msg_out = dumps(msg)

    def send_msg(self):
        name = input('Name please> ')
        msg = input('Msg> ')
        self.f_msg({'cmd':'send_msg', 'from':'Igor',
                     'msg':msg, 'adr':name, 'time':'time'})

    def auth(self):
        log = input('login> ')
        pas = input('pasw> ')

        self.f_msg({'cmd':'auth', 'login':log.strip(), 'pasw':pas.strip()})

    def regis(self):
        log = input('login> ')
        pas = input('pasw> ')
        nic = input('nick> ')
        self.f_msg({'cmd':'reg', 'login': log.strip(),
         'nick': nic.strip(), 'pasw': pas.strip()})


    def get_fr(self):
        self.f_msg({'cmd':'get_fr'})

    def get_msg(self):
        if (self.msg_out):
            res = self.msg_out
            self.msg_out = None
            return (res)
        else:
            return
    def quit_m(self):
        self.f_msg({'cmd':'quit'})

