from application import app, db
from application.models import Tasks
from application.forms import CreateForm, UpdateForm
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('read'):
def read():
    