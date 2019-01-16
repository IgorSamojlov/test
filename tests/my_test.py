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
        s.ws = mws.Ws()
        s.us_on['78ae236b5255425682defa181e2c8d98'] = 'ws'
        s.us_on['a6d2ea43c4234109a0873aa00d400a19'] = 'ws'

    def setup_method(self):
        pass

    def test_auth(self):
        pass


    def test_regis(self):
        msg = {'cmd':'reg', 'name':'Igo', 'pasw':'11111',
         'login':'Igoryan', 'nick':'nick'}
        assert sq.sql_regis(msg) == 0

    def test_regiss(self):
        s.msg_in = {'cmd':'reg', 'name':'Igorr', 'pasw':'11111',
         'login':'Igoryan', 'nick':'nickkk'}
        s.regis()
        assert s.msg_out != None





