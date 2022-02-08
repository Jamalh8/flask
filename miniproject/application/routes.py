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

from asyncio import tasks
from application import app, db
from application.models import Task

@app.route('/add/<task>')
def add(task):
    new_task = Task.query.first()
    new_task.name = task
    db.session.add()
    db.session.commit()
    return f"Added {new_task.name} to the database"

@app.route('/read')
def read():
    all_task = Task.query.all()
    task_string = ""
    for task in all_task:
        task_string += "<br>"+ task.name
    return task_string

# @app.route('/update/<task>')
# def add(task):
#     new_task = Task.query.first()
#     new_task.name = task
#     db.session.commit()
#     return f"Your task has now been updated to {new_task.name}"

# @app.route('/update/<name>')
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     db.session.commit()
#     return first_game.name