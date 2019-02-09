import readline
from command import Mcmd
from cmdinp import Cmd_inp
from json import dumps

def start_clie(state, ws):

    com = Cmd_inp(['_auth', '_reg', '_get', '_get_fr'])
    readline.set_completer(com.completer)
    readline.parse_and_bind('tab: complete')
    cmd = Mcmd()

    print ('For exit > q')
    ws.send(dumps({'cmd':'auth', 'login':'Igor', 'pasw':'11111'}))

    while True:

        command = input('> ')
        if (command == 'q' or command == 'quit' or command == 'exit'):
            cmd.read_msg('q')
            ws.send(cmd.get_msg())
            ws.close()
            break

        cmd.read_msg(command)

        message = cmd.get_msg()
        if (message) and (state):
            ws.send(message)
        elif not (message):
            print(command, ' not command, press Tab double\n')
        elif not(state):
            print ('Client offline\n')
