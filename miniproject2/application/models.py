from application import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50))

class Task_done(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_done = db.Column(db.String(50))