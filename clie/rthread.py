from threading import Thread
from json import loads
from json import dumps
from colorama import Fore, Style

class Rthread (Thread):
    def __init__(self, ws, friend):
        Thread.__init__(self)
        self.ws = ws
        self.msg = None
        self.fr = friend

    def run(self):

        while True:
            try:
                temp = self.ws.recv()
            except Exception as e:
                print(e)
                print ('Run is over\n')
                break
            if (temp):
                self.msg = loads(temp)
                temp = None #?????????????????????????????
            self.read_msg()

    def read_msg(self):
        print (self.msg)
        if (self.msg['cmd'] == 'auth'):
            print('Message from server: auth is:', self.msg['answer'])
        elif(self.msg['cmd'] == 'msg'):
            print('Message from', self.msg['from'], ' ', self.msg['msg'])
        elif (self.msg['cmd'] == 'reg'):
            print ('Registration is ', self.msg['answer'])
        elif (self.msg['cmd'] == 'get_fr'):
            self.show_friends(self.msg['friends'], self.msg['friends_on'])

    def show_friends(self, all_fr, fr_on):
        if (all_fr and fr_on):
            for f in all_fr:
                for a in fr_on:
                    print(Fore.GREEN + f)
                else:
                    print(Fore.RED + f)
        elif not fr_on and all_fr:
            for f in all_fr:
                print(Fore.RED + f)
        print(Style.RESET_ALL)
