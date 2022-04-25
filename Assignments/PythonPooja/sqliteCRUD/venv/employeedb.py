import sqlite3
con=sqlite3.connect('employee.db')

print("Database connected")
cur=con.cursor()
cur.execute("CREATE TABLE Eployees(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,email TEXT, address TEXT)")

con.commit()
con.close()