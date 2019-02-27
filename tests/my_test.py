import pytest
from db import msq
from serv import msgworker
from json import dumps
from json import loads
from tests import mws
from serv import myusers

server_worker = msgworker.MsgWorker()
sql_worker = msq.SqlWorker()
my_user = myusers.MyUser(3)

class Test_Serv(object):

    def setup(self):
        pass
    def setup_method(self):
        pass
    def test_regis(self):
        pass
    def test_get_fr(self):
        pass
    def test_add_message(self):
        pass
    def test_check_msg(self):
        pass
    def test_user(self):
        for i in range(0, 3):
            ws = 'ws_' + str(i)
            assert my_user.add_user('Kolya', ws) == True
            assert my_user.del_user_by_name('Kolya') == None

