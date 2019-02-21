import pytest
from db import msq
from serv import msgworker
from json import dumps
from json import loads
from tests import mws

s = msgworker.Msg_worker()
sq = msq.Sql_worker()

class Test_serv(object):

    def setup(self):
        #s.ws = mws.Ws()
        s.ws = '22222'
        s.us_on = {'11111':'Ann', '22222':'Igor'}
        s.us_on_rev = {'Ann':'11111', 'Igor':'22222'}
    def setup_method(self):
        pass

    def test_auth(self):
        pass


    def test_regis(self):
        pass

    def test_get_fr(self):
        assert s.get_fr() == {'Ann'}




