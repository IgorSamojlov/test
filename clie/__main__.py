from json import loads
from json import dumps

from clieworker import Clieworker

def main():
    from websocket import create_connection

    try:
        ws = create_connection("ws://localhost:5000")
        clie = Clieworker(ws)
        clie.run('On')
        print('Starting the client')
    except ConnectionRefusedError:
        print ('Please check the server\n')
        clie = Clieworker(None)
        clie.run(None)

if __name__ == '__main__':
    main()
