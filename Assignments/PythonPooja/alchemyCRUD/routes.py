from flask import Flask, redirect, url_for, render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///students.sqlite3'

db=SQLAlchemy(app)
class students(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    city=db.Column(db.String(50))
    def __init__(self,name,city):
        self.name=name
        self.city=city

@app.route('/')
def show_all():
    return render_template('show.html',student=students.query.all())

@app.route('/createdb')
def create():
    db.create_all()
    return redirect(url_for('show_all'))

@app.route('/new',methods=['POST','GET'])
def new_student():
    if request.method =='POST':
        name=request.form['name']
        city=request.form['city']
        newstudent=students(name=name,city=city)
        db.session.add(newstudent)
        db.session.commit()
        return redirect(url_for('show_all'))
    return render_template('new.html')

if __name__=='__main__':
    app.run(debug=True)

