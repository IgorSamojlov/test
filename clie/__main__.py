from json import loads
from json import dumps

from rthread import Rthread
from startclie import start_clie


def main():
    from websocket import create_connection

    try:
        ws = create_connection("ws://localhost:5000")

    except ConnectionRefusedError:
        print ('Please check the server\n')
        start_clie(False, None)
        print ('Good by\n')
        return(None)

    reciving_msg = Rthread(ws)
    reciving_msg.start()

    start_clie(True, ws)

if __name__ == '__main__':
    main()
