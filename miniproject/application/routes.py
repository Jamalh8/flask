# from application import app, db
# from application.models import Games

# @app.route('/add')
# def add():
#     new_game = Games(name="New Game")
#     db.session.add(new_game)
#     db.session.commit()
#     return "Added new game to database"

# @app.route('/read')
# def read():
#     all_games = Games.query.all()
#     games_string = ""
#     for game in all_games:
#         games_string += "<br>"+ game.name
#     return games_string

# @app.route('/update/<name>')
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     db.session.commit()
#     return first_game.name

from application import app, db
from application.models import Task

@app.route('/add')
def add():
    new_task = Task(task_name="New task")
    db.session.add(new_task)
    db.session.commit()
    return "Added this task to your to do list"

@app.route('/read')
def read():
    all_tasks = Task.query.all()
    task_string = ""
    for task in all_tasks:
        task_string += "<br>"+ task.task_name
    return task_string

@app.route('/update/<task_name>')
def update(task_name):
    first_task = Task.query.first()
    first_task.task_name = task_name
    db.session.commit()
    return first_task.task_name

@app.route('/count')
def count():
    number_of_tasks = Task.query.count()
    return str(number_of_tasks)

@app.route('/delete')
def delete():
    first_task = Task.query.first()
    db.session.delete(first_task)
    db.session.commit()
    return "You've deleted the first task on database"