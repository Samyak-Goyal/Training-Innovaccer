from crypt import methods
from flask import Flask, make_response, render_template, request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/setcookie',methods=['POST'])
def setCookie():
    if request.method=='POST':
        user=request.form['userid']
        resp=make_response(render_template('readcookie.html'))
        resp.set_cookie('userId',user) 
        return resp   

@app.route('/getcookie')
def getcookie():
    userid=request.cookies.get('userId')
    return '<h1>Cookie found: '+userid+'</h1>'


if __name__=='__main__':
    app.run(debug=True)
