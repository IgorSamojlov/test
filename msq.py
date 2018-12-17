import sqlite3

def add(mes):
    conn = sqlite3.connect('new.db')
    cursor = conn.cursor()

    sql = "INSERT INTO table1 VALUES (?,?,?)"

    cursor.execute(sql, mes)
    conn.commit()
    conn.close()



