from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField,FloatField

app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class InfoForm(FlaskForm):

    name = StringField('Enter the operation name.')
    num1 = IntegerField('Number1')
    num2 = FloatField('Number2')
    add = SubmitField('add')
    sub = SubmitField('sub')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = False
    form = InfoForm()
    sum=0
    sub=0
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = name
        n1 = form.num1.data
        n2 = form.num2.data
        sum = n1+n2
        sub = n1-n2
        print sum
        print sub
    return render_template('dis2.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
