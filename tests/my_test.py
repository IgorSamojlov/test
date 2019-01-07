import pytest
from db import msq
from serv import cserv
from json import dumps
from json import loads
from tests import mws

s = cserv.M_server()
sq = msq.Sql_worker()

class Test_serv(object):

    def setup(self):
        s.ws = mws.Ws()
        s.us_on['78ae236b5255425682defa181e2c8d98'] = 'ws'
        s.us_on['a6d2ea43c4234109a0873aa00d400a19'] = 'ws'

    def setup_method(self):
        pass

    def test_auth(self):
        s.msg_in = {'cmd':'auth','id':'da787eae867843a7bb10131acc4a2da4',
        'pasw':'11111'}
        assert s.auth() == None

    def test_send_msg(self):
        s.msg_in = {'cmd': 'send_msg', 'msg':'Hello', 'time':'time',
        'adr':'aaa', 'from':'da787eae867843a7bb10131acc4a2da4'}

        assert s.send_msg() == None

    def test_us_on(self):
        s.msg_in = {'cmd': 'get_user', 'us': ['78ae236b5255425682defa181e2c8d98',
        'a6d2ea43c4234109a0873aa00d400a19']}

        assert s.get_user_on() == None
        assert len(s.msg_out['us_on']) > 0

