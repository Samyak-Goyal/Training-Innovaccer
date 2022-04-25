from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)

@app.route('/result',methods=['POST','GET'])    
def result():
    if request.method=='POST':
        # name=request.form['nm']
        # phy=request.form['py']
        # chem=request.form['ch']
        # mat=request.form['ma']
        # dict={'name':name ,'maths':mat,'chem':chem, 'physics':phy}
        results=request.form
        return render_template('result.html', result=results)


if __name__=='__main__':
    app.run(debug=True)             