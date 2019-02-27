import logging
import sqlite3
import uuid
import sys
import os

class SqlWorker:
    def __init__(self):

        self.conn = sqlite3.connect(self.file_name())
        self.cursor = self.conn.cursor()

    def app_dir(self):
        return (os.path.dirname(os.path.realpath(__file__)))

    def file_name(self):
        env = os.getenv('ENV', 'nw')
        file = f'{env}.db'
        return os.path.join(self.app_dir(), file)

    def sql_auth(self, msg):
        sql = 'SELECT pasw, nick FROM users WHERE login=?'
        self.cursor.execute(sql, [msg['login']])
        temp = self.cursor.fetchall()
        print(temp)
        if (temp) and (temp[0][0] == msg['pasw']):
            return(temp[0][1])
        else:
            return (None)

    def sql_us_on(self, msg, adr):
        self.conn.execute(
            'INSERT INTO user_on (login, remote_address) values (?,?)',
        (msg['login'], adr))
        self.conn.commit()

    def sql_us_on_del(self, ide):
        pass

    def sql_regis(self, msg):
        sql = 'SELECT EXISTS(SELECT * FROM users WHERE login=? LIMIT 1)'

        self.cursor.execute(sql, [msg['login']])
        temp = self.cursor.fetchall()
        if ((temp[0][0]) == 0):
            sql = 'INSERT INTO users (nick, login, pasw) values (?,?,?)'
            self.conn.execute(Sql, [msg['nick'], msg['login'], msg['pasw']])
            self.conn.commit()
            return(True)
        else:
            return(False)

    def sql_add_friends(self, msg):
        pass
        self.cursor.execute(sql)
        self.conn.commit()

    def sql_get_fr(self, log):
        pass

    def format_user(self, user):
        return (list(x[0] for x in user))

    def sql_add_message(self, msg):
        sql = 'INSERT INTO messages (user_from, to_user, message, m_time, read)\
         values (?, ?, ?, ?, ?)'
        self.cursor.execute(sql, [msg['from'], msg['adr'],
                                 msg['msg'], msg['time'], 'n'])
        self.conn.commit()


    def sql_read_messages(self, msg):
        sql = 'SELECT * FROM messages WHERE to_user=? AND read="n"'
        self.cursor.execute(sql, [msg['login']])
        temp = (self.cursor.fetchall())
        sql = 'UPDATE messages SET read="y" WHERE to_user=?'

        self.cursor.execute(sql, [msg['login']])
        self.conn.commit()

    def get_table_name(self, msg):
        return(msg['from'] + '_' + msg['adr'] + '_' + 'messages')

    def __del__(self):
        self.conn.close()
