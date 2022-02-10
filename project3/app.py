from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SECRET_KEY'] = '007'

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

class TaskForm(FlaskForm):
    title = StringField('Title of task')
    task_desc = StringField('Description of task')
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = TaskForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            post = Post(title = form.title.data,
                task_desc = form.task_desc.data,
                )
            db.session.add(post)
            db.session.commit()
            return render_template('home.html', form=form)