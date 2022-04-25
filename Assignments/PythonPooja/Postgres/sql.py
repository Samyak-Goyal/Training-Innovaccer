import psycopg2 

def create():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students(id SERIAL PRIMARY KEY,first_name TEXT,last_name TEXT, grade INTEGER, total_score INTEGER, gender TEXT, result TEXT,age INTEGER)")
    conn.commit()
    conn.close()

create()

def insert(firstname,lastname,grade,totalscore,gender,result,age):   
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO students(first_name, last_name, grade,total_score,gender,result,age) VALUES(%s,%s,%s,%s,%s,%s,%s)",(firstname,lastname,grade,totalscore,gender,result,age))
    conn.commit()
    conn.close()

# insert("sam","mkkd",8,80,"Male","pass",14)
# insert("jay","mkkd",10,80,"Male","pass",14)
# insert("xfxf","dvdv",3,56,"Male","pass",4)
# insert("frfr","wffr",8,40,"Male","pass",10)
# insert("gth","tht",6,80,"Male","pass",8)
# insert("dwed","wdwd",1,80,"Male","pass",14)
# insert("ruhi","wdwd",7,80,"Female","pass",14)


def view():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM students")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def viewbyGrade():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM students WHERE grade=8")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# print(viewbyGrade())

def viewbyLastname():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM students WHERE last_name LIKE 'm%'")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows


# print(viewbyLastname())

def shift():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE students SET grade=5 WHERE first_name='jay' AND grade=10")
    conn.commit()
    conn.close()

# shift()

def deletebelow5():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM students WHERE age<5")
    conn.commit()
    conn.close()

# deletebelow5()    

def updateFail():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE students SET result='fail' WHERE total_score<45")
    conn.commit()
    conn.close()

# updateFail()


def updateHold():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE students SET result='hold' WHERE age<10")
    conn.commit()
    conn.close()

# updateHold()




def deletegrade1():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM students WHERE grade=1")
    conn.commit()
    conn.close()


# deletegrade1()

def updateHoldTomale():
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE students SET gender='male1' WHERE result='hold'")
    conn.commit()
    conn.close()

# updateHoldTomale()

# def updateLastName():
#     conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
#     cur=conn.cursor()
#     cur.execute("UPDATE students SET last_name='new' WHERE first_name='ruhi'")
#     conn.commit()
#     conn.close()

# updateLastName()

def updateLastNameR(firstname,lastname):
    conn=psycopg2.connect("dbname='python_test' user='samyak' password='123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE students SET last_name=%s WHERE first_name=%s",(lastname,firstname))
    conn.commit()
    conn.close()
updateLastNameR("ruhi","abc")

print(view())

