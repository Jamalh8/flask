# from application import db
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     task = db.Column(db.String(50))

# class Task_done(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     task_complete = db.Column(db.String(50))

# class TaskForm(FlaskForm):
#     title = StringField('Title of task')
#     task_desc = StringField('Description of task')
#     submit = SubmitField('Submit')