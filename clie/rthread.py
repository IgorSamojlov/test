from threading import Thread
from recvmsg import read_msg
from json import loads
from json import dumps

class Rthread (Thread):
    def __init__(self, ws):
        Thread.__init__(self)
        self.ws = ws

    def run(self):

        while True:
            try:
                temp = self.ws.recv()
            except Exception as e:
                print(e)
                print ('Run is over\n')
                break
            if (temp):
                msg = loads(temp)
                temp = None #?????????????????????????????
            print('Message from server ', msg)
            read_msg(msg)
