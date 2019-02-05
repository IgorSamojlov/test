from json import load
from json import dumps

class Mcmd():
    def __init__(self):
        self.cmd = None
        self.msg_out = None

    def read_msg(self, cmd):
        if (cmd == '_auth'):
            self.auth()
        elif (cmd == '_reg'):
            self.regis()
        elif (cmd == '_get_fr'):
            self.get_fr()
        elif (cmd == 'q'):
            self.quit_m()

    def f_msg(self, msg):
        self.msg_out = dumps(msg)

    def auth(self):
        log = input('login> ')
        pas = input('pasw> ')

        self.f_msg({'cmd':'auth', 'login':log.strip(), 'pasw':pas.strip()})

    def regis(self):
        log = input('login> ')
        pas = input('pasw> ')
        nic = input('nick> ')

    def get_fr(self):
        self.f_msg({'cmd':'get_fr'})


    def regis(self):
        self.f_msg({'cmd':'reg', 'login': log.strip(),
         'nick': nic.strip(), 'pasw': pas.strip()})

    def get_msg(self):
        if (self.msg_out):
            res = self.msg_out
            self.msg_out = None
            return (res)
        else:
            return
    def quit_m(self):
        self.f_msg({'cmd':'quit'})

