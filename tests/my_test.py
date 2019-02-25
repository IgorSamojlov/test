import pytest
from db import msq
from serv import msgworker
from json import dumps
from json import loads
from tests import mws
from serv import myusers

s = msgworker.Msg_worker()
sq = msq.Sql_worker()
mu = myusers.MyUser(3)
ws = mws.Ws()
ws.open = 'saas'

class Test_serv(object):

    def setup(self):

        s.us_on = {'11111':'Ann', '22222':'Igor'}
        s.us_on_rev = {'Ann':'11111', 'Igor':'22222'}

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
        for i in range(0, 4):
            ws = 'ws_' + str(i)
            assert mu.add_user('Kolya', ws) == True


