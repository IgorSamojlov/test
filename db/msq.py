import sqlite3
import uuid
import sys
import os

class Sql_worker():
    def __init__(self):
        print ('conn')

        self.conn = sqlite3.connect(self.file_name())
        self.cursor = self.conn.cursor()

    def app_dir(self):
        return (os.path.dirname(os.path.realpath(__file__)))

    def file_name(self):
        env = os.getenv('ENV', 'nw')
        file = f'{env}.db'
        return os.path.join(self.app_dir(), file)

    def msg_in_qu(self, msg):

        self.conn.execute(
            'INSERT INTO messages (user, from_ident, message, d_time) values (?,?,?,?)',
        (msg['adr'], msg['from'], msg['msg'], msg['time']))
        self.conn.commit()

    def sql_get_message(self, msg):

        sql = "SELECT * FROM messages WHERE user=?"
        self.cursor.execute(sql, msg['id'])
        temp = (cursor.fetchall())

        sql = 'DELETE FROM messages WHERE user=?'
        self.cursor.execute(sql, msg['id'])

        self.conn.commit()

        return (temp)

    def sql_auth(self, msg):
        sql = 'SELECT pasw FROM users WHERE login=?'
        self.cursor.execute(sql, [msg['login']])
        temp = self.cursor.fetchall()
        if (temp[0][0] == msg['pasw']):
            print (temp[0][0])
            return(True)
        else:
            return(False)

    def sql_us_on(self, msg, adr):
        self.conn.execute(
            'INSERT INTO users_on (ident, remote_address) values (?,?)',
        (msg['id'], adr))
        self.conn.commit()

    def sql_us_on_del(self, ide):
        sql = "DELETE FROM users_on WHERE ident=?"
        for i in ide:
            self.conn.execute(sql, [i])
            self.conn.commit()


    def sql_regis(self, msg):

        sql = 'SELECT EXISTS(SELECT * FROM users WHERE login=? LIMIT 1)'

        self.cursor.execute(sql, [msg['login']])
        temp = self.cursor.fetchall()
        if ((temp[0][0]) == 0):
            sql = 'INSERT INTO users (nick, login, pasw) values (?,?,?)'
            self.conn.execute(sql, [msg['nick'], msg['login'], msg['pasw']])
            self.conn.commit()
            return(True)

        else:
            return(False)



    def __del__(self):
        print ('Sql del')
        self.conn.close()


