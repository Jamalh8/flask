from application import app, db
from application.models import Task
from miniproject2.application.models import Task_done, Task_left

@app.route('/')
@app.route('/home')
def home():
    return f'Welcome to the home page'
def all_task():
    all_task = Task.query.all()
    task_string = ""
    for task in all_task:
        task_string += "<br>"+ task.name
    return f'{task_string} - these are your remaining tasks'
def task_done():
    task_done = Task_done.query.all()
    task_done_string = ""
    for task_done in all_task_left:
        task_done_string += "<br>" + task_done.name
    return f'{task_done_string} - These are the tasks you completed'


# @app.route('/update/<task>')
# def update(task):
#     return 'This has been added to your list'

# @app.route('/delete')
# def delete():
#     first_task = Task.query.first()
#     db.session.delete(first_task)
#     db.session.commit()
#     return "You've deleted the first task on database"
