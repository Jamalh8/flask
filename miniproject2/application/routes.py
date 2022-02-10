from application import app, db
from application.models import Task, Task_done

@app.route('/')
@app.route('/home')
def home():
    all_task = Task.query.all()
    task_finished = Task_done.query.all()
    task_string = ""
    task_finished_string = ""
    for task in all_task:
        task_string += "<br>"+ task.task
    for task_complete in task_finished:
        task_finished_string += "<br>"+ task_complete.task_complete
    return f"<b>These are your remaining tasks:</b> {task_string} \n <b>These are the tasks you've completed:</b> {task_finished_string}"

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
    return task_update.task

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


