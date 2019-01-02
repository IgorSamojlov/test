from db import msq
from serv import cserv

a = cserv.M_server()

msg = [{'cmd':'auth','id':'da787eae867843a7bb10131acc4a2da4','pasw':'11111'},
{'cmd':'quit', 'id':'da787eae867843a7bb10131acc4a2da4'},
{'cmd': 'get_user'}]

a.msg_in = msg[1]

def test_auth():
    a.read_msg()

