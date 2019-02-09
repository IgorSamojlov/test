from json import loads
from json import dumps

from rthread import Rthread
from startclie import start_clie

def main():
    from websocket import create_connection
    ws = create_connection("ws://localhost:5000")

    reciving_msg = Rthread(ws)
    reciving_msg.start()

    start_clie()

if __name__ == '__main__':
    main()
