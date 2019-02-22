import sqlite3
import uuid
import sys
import os

class Sql_worker():
    def __init__(self):

        self.conn = sqlite3.connect(self.file_name())
        self.cursor = self.conn.cursor()
        print ('DB is open')

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
            self.add_table_user(msg)
            return(True)
        else:
            return(False)

    def add_table_user(self, msg):
        table_name = (msg['login'] + '_friends')
        sql = 'CREATE TABLE {} (name text)'.format(table_name)

        self.cursor.execute(sql)
        self.conn.commit()

    def sql_get_fr(self, log):
        table = log + '_friends'
        sql = 'SELECT login FROM {}'.format(table)
        self.cursor.execute(sql)
        temp =(self.cursor.fetchall())
        return (self.format_user(temp))

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
        print (temp)

    def get_table_name(self, msg):
        return(msg['from'] + '_' + msg['adr'] + '_' + 'messages')

    def __del__(self):
        print ('Sql del')
        self.conn.close()


