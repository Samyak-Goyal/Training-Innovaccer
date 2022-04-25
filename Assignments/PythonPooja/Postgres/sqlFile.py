import psycopg2 

def create():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY,first_name TEXT,last_name TEXT, age INTEGER)")
    conn.commit()
    conn.close()

def insert(firstname,lastname,age):   
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO users(first_name, last_name, age) VALUES(%s,%s,%s)",(firstname,lastname,age))
    conn.commit()
    conn.close()

# insert("fef","efefe",23)    

def view():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM users WHERE age<30")
    conn.commit()
    conn.close()

def update(firstname,age):
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE users SET age=%s WHERE first_name=%s",(age,firstname))
    conn.commit()
    conn.close()


# delete()
# update("fef",32)
print(view())    