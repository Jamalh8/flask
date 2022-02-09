from application import app, db
from application.models import Task, Task_done

@app.route('/')
@app.route('/home')
# def all_task():
#     all_task = Task.query.all()
#     task_string = ""
#     for task in all_task:
#         task_string += "<br>"+ task.task
#     return f"These are your remaining tasks:\n{task_string}"
# def task_done():
#     task_finish = Task_done.query.all()
#     task_finish_string = ""
#     for task_complete in task_finish:
#         task_finish_string += "<br>" + task_complete.task_complete
#     return f'These are the tasks you have compeleted:\n{task_finish_string}'

def all_task():
    all_task = Task.query.all()
    task_string = ""
    for task in all_task:
        task_string += "<br>"+ task.task
    return f"These are your remaining tasks:\n{task_string}"
    
# def task_done():
#     task_finish = Task_done.query.all()
#     task_finish_string = ""
#     for task_complete in task_finish:
#         task_finish_string += "<br>" + task_complete.task_complete
#     return f'These are the tasks you have compeleted:\n{task_finish_string}'


@app.route('/add')
def add():
    new_task = Task(task="New task")
    db.session.add(new_task)
    db.session.commit()
    return "Added new task to database"

@app.route('/complete')
def complete():
    task_finish = Task_done(task_complete="Task Complete")
    db.session.add(task_finish)
    db.session.commit()
    return "This task is now complete"

@app.route('/delete')
def delete():
    first_task = Task.query.first()
    db.session.delete(first_task)
    db.session.commit()
    return "You've deleted the first task on database"

@app.route('/update/<task>')
def update(task):
    task_update = Task.query.first()
    task_update.task = task
    db.session.commit()
    return task_update.task


