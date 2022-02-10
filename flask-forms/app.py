from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = '007'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    dob = DateField("D.O.B")
    fav_num = IntegerField ("Your favorite number?")
    fav_food = SelectField ("Pick your favorite food", choices= [(1, "Pizza"), (2, "Burger"), (3, "Chicken")])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        fav_num = form.fav_num.data
        fav_food = form.fav_food.data

        if len(first_name) == 0 or len(last_name) == 0 or fav_num == None:
            message = "Please supply all details to continue"
        else:
            message = f'Thank you. Here is your personalised username {fav_num}{first_name}{fav_food}'

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')