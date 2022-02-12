from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

class CreateForm(FlaskForm):
    name= StringField('Title of task', validators=[DataRequired(), Length(min=2, max=30)])
    description = StringField('Description of task', validators=[DataRequired(), Length(min=2,max=100)])
    submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
    name= StringField('Title of task', validators=[DataRequired(), Length(min=2, max=100)])
    description = StringField('Description of task', validators=[DataRequired(), Length(min=2,max=100)])
    complete = BooleanField('Complete')
    submit = SubmitField('Submit')