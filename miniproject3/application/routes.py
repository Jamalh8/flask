from flask import render_template, request
from application import app, db
from application.models import Task, Task_done
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TaskForm(FlaskForm):
    title = StringField('Title of task')
    task_desc = StringField('Description of task')
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def post():
    message = ""
    form = TaskForm()

    if request.method == 'POST':
        title = form.title.data
        task_desc = form.task_desc.data
        if len(title) == 0 or len(task_desc) == 0:
            message = "Please supply all details of your task"
        else:
            message = f"Thank you. I've added <b> {title} </b> \n {task_desc} to the database"

    return render_template('home.html', form=form, message=message)

@app.route('/compare')
def compare():
    all_task = Task.query.all()
    task_finished = Task_done.query.all()
    task_string = ""
    task_finished_string = ""
    for task in all_task:
        task_string += "<br>"+ task.task
    for task_complete in task_finished:
        task_finished_string += "<br>"+ task_complete.task_complete
    return f"<b>These are your remaining tasks:</b> {task_string} <br><br><b>These are the tasks you've completed:</b> {task_finished_string}"

@app.route('/add')
def add():
    new_task = Task(task="New task")
    db.session.add(new_task)
    db.session.commit()
    return "New task added"

@app.route('/update/<task>')
def update(task):
    task_update = Task.query.first()
    task_update.task = task
    db.session.commit()
    return f'{task_update.task.upper()} has been updated on your task list'

@app.route('/delete')
def delete():
    first_task = Task.query.first()
    db.session.delete(first_task)
    db.session.commit()
    return "You've deleted the first task on database"

@app.route('/done')
def done():
    task_finish = Task_done(task_complete="Task Done")
    db.session.add(task_finish)
    db.session.commit()
    return "This task is now done"

@app.route('/completed')
def completed():
    task_finished = Task_done.query.first()
    db.session.delete(task_finished)
    db.session.commit()
    return "You've deleted the completed task"


