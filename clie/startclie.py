import readline
from command import Mcmd
from cmdinp import Cmd_inp

def start_clie(state, ws):

    com = Cmd_inp(['_auth', '_reg', '_get'])
    readline.set_completer(com.completer)
    readline.parse_and_bind('tab: complete')
    cmd = Mcmd()

    print ('For exit > q')

    while True:

        command = input('> ')
        if (command == 'q'):
            break

        cmd.read_msg(command)

        message = cmd.get_msg()
        if (message) and (state):
            ws.send(message)
        elif not (message):
            print(command, ' not command, press Tab double\n')
        elif not(state):
            print ('Client offline\n')
