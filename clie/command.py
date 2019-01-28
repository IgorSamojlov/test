from json import load
from json import dumps

class Mcmd():
    def __init__(self):
        self.cmd = None
        self.msg_out = None

    def read_msg(self, cmd):
        if (cmd == '_auth'):
            self.auth()

    def f_msg(self, msg):
        self.msg_out = dumps(msg)

    def auth(self):
        log = input('login> ')
        pas = input('pasw> ')

        self.f_msg({'cmd':'auth', 'login':log.strip(), 'pasw':pas.strip()})

    def get_msg(self):
        if (self.msg_out):
            res = self.msg_out
            self.msg_out = None
            return (res)
        else:
            return
