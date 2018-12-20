from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    n1=55
    n2=22
    total=n1+n2
    diff=n1-n2
    mul=n1*n2
    div=float(n1/n2)
    return render.template('mathcal.html',**locals())
if __name__ =='__main__':
    app.run()
