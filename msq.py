import sqlite3
import uuid

def load(ls):
    conn = sqlite3.connect('new.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * from users")

    result = cursor.fetchall()
    for r in result:
        ls[r[4]] = {'name':r[0], 'surname': r[1], 'nick':r[2], 'pasw':r[3]}

    conn.close()

def add_message(user, adr, msg, d_time):
    conn = sqlite3.connect('new.db')
    cursor = conn.cursor()

    conn.execute('INSERT INTO messages (user, address, message, d_time) values (?,?,?,?)',
     (user, adr, msg, d_time))
    conn.commit()

    conn.close()

def get_message(ident):
    conn = sqlite3.connect('new.db')
    cursor = conn.cursor()

    sql = "SELECT * FROM messages WHERE user=?"
    cursor.execute(sql, [ident])
    temp = (cursor.fetchall())

    sql = "DELETE FROM messages WHERE user=?"
    cursor.execute(sql, [ident])

    conn.commit()

    conn.close()
    return (temp)
