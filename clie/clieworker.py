from rthread import Rthread
from cmdinp import Cmd_inp
from command import Mcmd

from json import dumps
from json import loads
import readline


class Clieworker():

    def __init__(self, ws):
        self.websocket = ws
        self.friends = {}
        self.read_msg_worker = Rthread(self.websocket, {})
        self.read_msg_worker.start()

    def run(self, state):

        self.auto_tab(['_auth', '_reg', '_get', '_get_fr'])
        cmd = Mcmd()

        print ('For exit > q')
        self.websocket.send(dumps({'cmd':'auth', 'login':'Igor', 'pasw':'11111'}))

        while True:
            command = input('> ')
            if (command == 'q' or command == 'quit' or command == 'exit'):
                cmd.read_msg('q')
                self.websocket.send(cmd.get_msg())
                self.websocket.close()
                break

            cmd.read_msg(command)

            message = cmd.get_msg()
            if (message) and (state):
                self.websocket.send(message)
            elif not (message):
                print(command, ' not command, press Tab double\n')
            elif not(state):
                print ('Client offline\n')


    def auto_tab(self, command):
        com = Cmd_inp(command)
        readline.set_completer(com.completer)
        readline.parse_and_bind('tab: complete')

