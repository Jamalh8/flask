from application import app, db
from application.models import Tasks
from application.forms import CreateForm, UpdateForm
from flask import render_template, redirect, url_for, request

@app.route('/create', methods=['GET', 'POST'])
def create():
    createform = CreateForm()

    if createform.validate_on_submit():
        task = Tasks(name=createform.name.data, description=createform.description.data)
        db.session.add(task)
        db.session.commit()
        # Instead of rendering a template, the next line redirects the user to the endpoint for the function called 'read'.
        return redirect(url_for('read'))
    return render_template('create.html', form=createform)

@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    tasks = Tasks.query.all()
    return render_template('read.html', tasks=tasks)

@app.route('/update/<name>', methods=['GET', 'POST'])
def update(name):
    updateform = UpdateForm()
    task = Tasks.query.filter_by(name=name).first()
    
    # Prepopulate the form boxes with current values when they open the page.
    if request.method == 'GET':
        updateform.name.data = task.name
        updateform.description.data = task.description
        return render_template('update.html', form=updateform)
    
    # Update the item in the databse when they submit
    else:
        if updateform.validate_on_submit():
            task.name = updateform.name.data
            task.description = updateform.description.data
            task.completed = updateform.completed.data
            db.session.commit()
            return redirect(url_for('read'))
    

@app.route('/delete/<name>', methods=['GET', 'POST'])
def delete(name):
        task = Tasks.query.filter_by(name=name).first()
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('read'))

@app.route('/complete/<name>', methods=['GET'])
def complete(name):
    task = Tasks.query.filter_by(name=name).first()
    task.completed = True
    db.session.commit()
    return redirect(url_for('read'))

@app.route('/incomplete/<name>', methods=['GET'])
def incomplete(name):
    task = Tasks.query.filter_by(name=name).first()
    task.completed = False
    db.session.commit()
    return redirect(url_for('read'))


