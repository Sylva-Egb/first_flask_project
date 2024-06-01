from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired

class TodoForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired(), Length(min=5, max=250)])
    submit = SubmitField('Submit')

