
import sqlite3
from flask import Flask,render_template,request,make_response, redirect,url_for

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')    

@app.route('/savedetails',methods=['POST'])
def saveDetails():
    msg='msg'
    if(request.method=='POST'):
        name=request.form['name']
        email=request.form['email']
        address=request.form['address']
        con=sqlite3.connect('employee.db')
        cur=con.cursor()
        cur.execute('INSERT INTO Eployees Values(NULL,?,?,?)',(name,email,address))
        con.commit()
        msg='Data added Successfully'
        con.close()
        return render_template('success.html',msg=msg)

# @app.route('/savedetails',methods=['POST'])
# def saveDetails():
#     msg='msg'
#     if(request.method=='POST'):
#         name=request.form['name']
#         email=request.form['email']
#         address=request.form['address']
#         con=sqlite3.connect('employee.db')
#         cur=con.cursor()
#         cur.execute('INSERT INTO Eployees Values(NULL,?,?,?)',(name,email,address))
#         con.commit()
#         msg='Data added Successfully'
#         con.close()
#         return render_template('success.html',msg=msg)

@app.route('/view')
def view():
    con=sqlite3.connect('employee.db')
    cur=con.cursor()
    cur.execute('SELECT * FROM Eployees')
    rows=cur.fetchall()
    con.close()
    return render_template('view.html',rows=rows)

@app.route('/delete/<id>')
def delete(id):
    con=sqlite3.connect('employee.db')
    cur=con.cursor()
    cur.execute('DELETE FROM Eployees WHERE id=?',(id,))
    con.commit()
    con.close()
    return redirect(url_for('view'))


if __name__=='__main__':
    app.run(debug=True)
