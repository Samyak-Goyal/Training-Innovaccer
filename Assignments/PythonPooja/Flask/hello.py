from crypt import methods
from os import abort
from flask import Flask, redirect, render_template, url_for, request

app=Flask(__name__)
@app.route("/hello/<name>")
def hello_world(name):
    return"Hello %s"%name

@app.route("/post/<int:postid>")
def hello_post(postid):
    return "Hello %s"%postid
# app.add_url_rule("/hello",view_func=hello_world)

@app.route("/admin")
def hello_admin():
    return"Hello admin" 

@app.route("/guest/<guest>")
def hello_guest(guest):
    return"Hello %s as guest"%guest
    
@app.route("/user/<name>")
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for("hello_guest",guest=name))    
 
@app.route('/login',methods=['POST','GET'])    
def login():
    if request.method=='POST':
        user=request.form['nm']
        if user=='admin':
            return redirect(url_for('success',name=user))
        else:
            abort(400)            
    else:
        user=request.args.get('nm')
        return redirect(url_for('success',name=user)) 


@app.route('/userData')
def userData():
    user=request.args.get('nm')
    return redirect(url_for('success',name=user)) 

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' %name  

@app.route('/')
def index():
    return render_template('hello.html')


if __name__=='__main__':
    app.run(host='127.0.0.1',port='5000',debug=True)    