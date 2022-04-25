import sqlite3

def createTable():
    conn=sqlite3.connect("lite2.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customer(firstname TEXT,lastname TEXT, age INT, gender TEXT) ")
    conn.commit()
    conn.close()

def insert(firstname,lastname,age,gender):
    conn=sqlite3.connect("lite2.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO customer VALUES(?,?,?,?) ",(firstname,lastname,age,gender))
    conn.commit()
    conn.close()

# createTable()  
# insert("Sam","awds",22,'Male')
# insert("ask","fvf",27,'Female')
# insert("adf","ede",24,'Male')
# insert("hhgb","jess",72,'Male')
# insert("wxcc","awswxds",12,'Male')
# insert("wswwd","efr",72,'Male')

def above50():
    conn=sqlite3.connect("lite2.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM customer WHERE age> 50")
    ans=cur.fetchall()
    conn.commit()
    conn.close()
    return ans

# print(above50())

def viewAll():
    conn=sqlite3.connect("lite2.db")
    cur=conn.cursor()
    cur.execute("SELECT rowid,* FROM customer ")
    ans=cur.fetchall()
    conn.commit()
    conn.close()
    return ans

# for v in viewAll():
#     print(v)

def viewStartwith():
    conn=sqlite3.connect("lite2.db")
    cur=conn.cursor()
    cur.execute("SELECT rowid,* FROM customer WHERE firstname LIKE 'a%' ")
    ans=cur.fetchall()
    conn.commit()
    conn.close()
    return ans
# for k in viewStartwith():
#     print(k)

def viewid(id):
    conn=sqlite3.connect("lite2.db")
    cur=conn.cursor()
    cur.execute("SELECT rowid,* FROM customer WHERE rowid=?",(id,))
    ans=cur.fetchall()
    conn.commit()
    conn.close()
    return ans

# print(viewid(4))


def updateLastname(id,lastname):
    conn=sqlite3.connect("lite2.db")
    cur=conn.cursor()
    cur.execute("UPDATE customer SET lastname=? WHERE rowid=?",(lastname,id))
    conn.commit()
    conn.close()

# updateLastname(5,"hello")

def deletewithLastname(lastname):
    conn=sqlite3.connect("lite2.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM customer WHERE lastname=?",(lastname,))
    conn.commit()
    conn.close()

# deletewithLastname("jess")

def updateGender(gender):
    conn=sqlite3.connect("lite2.db")
    cur=conn.cursor()
    cur.execute("UPDATE customer SET gender=?",(gender,))
    conn.commit()
    conn.close()

# updateGender("others")

def updateGenderifless20(gender):
    conn=sqlite3.connect("lite2.db")
    cur=conn.cursor()
    cur.execute("UPDATE customer SET gender=? WHERE age< 20",(gender,))
    conn.commit()
    conn.close()

# updateGenderifless20("female")



for v in viewAll():
    print(v)