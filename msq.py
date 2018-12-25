import sqlite3
import uuid


class Sql_worker():
    def __init__(self, bd):
        self.conn = sqlite3.connect(bd)
        self.cursor = self.conn.cursor()

    def load(self, ls):

        cursor.execute("SELECT * from users")

        result = cursor.fetchall()
        for r in result:
            ls[r[4]] = {'name':r[0], 'surname': r[1], 'nick':r[2], 'pasw':r[3]}


    def add_message(self, user, adr, msg, d_time):

        self.conn.execute('INSERT INTO messages (user, address, message, d_time) values (?,?,?,?)',
        (user, adr, msg, d_time))
        self.conn.commit()

    def get_message(self, ident):

        sql = "SELECT * FROM messages WHERE user=?"
        self.cursor.execute(sql, [ident])
        temp = (cursor.fetchall())

        sql = "DELETE FROM messages WHERE user=?"
        self.cursor.execute(sql, [ident])

        self.conn.commit()

        return (temp)

    def sql_auth(self, ident, pasw):
        sql = "SELECT pasword FROM users WHERE uuid =?"
        self.cursor.execute(sql, [ident])
        temp = self.cursor.fetchall()
        if (temp[0][0] == pasw):
            print (temp[0][0])
            print (pasw)
            return(True)
        else:
            return(False)


    def __del__(self):
        print ('Sql del')
        self.conn.close()


