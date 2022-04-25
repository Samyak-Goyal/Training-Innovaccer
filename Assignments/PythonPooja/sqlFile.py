import sqlite3

def create():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()


def insert(item , quantity, price):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()



# insert("pens2",20,203)
# insert("books2",13,20.34)


def view():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("SELECT rowid,* FROM store WHERE item LIKE 'p%' ORDER BY item DESC")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def delete(id):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE rowid=?",(id,))
    conn.commit()
    conn.close()

def update(item,quantity,price):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

def update(id,item,quantity,price):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=?,item=? WHERE rowid=?",(quantity,price,item,id))
    conn.commit()
    conn.close()

def dropTable():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("DROP TABLE store")
    conn.commit()
    conn.close()

dropTable()    
# delete('pens2')
# delete(1)
# update('pens',23,23.34)
# update(2,'pens23',33,233.34)



for v in view():
    print(v)  
























