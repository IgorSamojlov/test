from db import msq
from serv import cserv
import json

a = cserv.M_server()
b = msq.Sql_worker()


msg = [{'cmd':'auth','id':'da787eae867843a7bb10131acc4a2da4','pasw':'11111'},
{'cmd':'quit', 'id':'da787eae867843a7bb10131acc4a2da4'},
{'cmd': 'get_user', 'us':['aa', 'aa', 'ss']},
{'cmd': 'send_msg', 'msg':'Hello', 'time':'time',
 'adr':'da787eae867843a7bb10131acc4a2ds4', 'from':'aaa'}]

temp_msg = json.dumps(msg[3])
t = json.loads(temp_msg)

a.msg_in = t

def test_bd():
    assert b.sql_add_message(t) == None

def test_auth():
    assert True

