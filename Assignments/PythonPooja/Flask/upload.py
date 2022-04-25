from crypt import methods
from unicodedata import name
from flask import Flask, render_template, request
app=Flask(__name__)


@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        fileData=request.files['file']
        fileData.save(fileData.filename)
        return render_template('success.html', name=fileData.filename)

if __name__=='__main__':
    app.run(debug=True)     