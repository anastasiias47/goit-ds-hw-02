import sqlite3

def create_db():
    with open('goit-ds-hw-02.sql', 'r') as f:
        sql = f.read()
    
    with sqlite3.connect('database1.db') as con:
        cur = con.cursor()
        cur.executescript(sql)

if __name__ == "__main__":
    create_db()