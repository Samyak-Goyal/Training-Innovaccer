from flask import Flask, render_template
app=Flask(__name__)

@app.route('/hello/<user>')
def index(user):
    return render_template('hello.html',name=user)

@app.route('/marks/<int:score>')
def marks(score):
    return render_template('marks.html',marks=score)

@app.route('/result') 
def result():
    dict={'maths':90,'chem':50, 'history':30}
    return render_template('result.html', result=dict)

@app.route('/')
def rootfile():
    return render_template('index.html')
    
if __name__=='__main__':
    app.run(host='127.0.0.1',port='8080',debug=True)     