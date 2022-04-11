from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    # image = StringField('Image', validators=[DataRequired()])
    # attending = BooleanField('Attending', validators=[DataRequired()])
    # favorite = BooleanField('Attending', validators=[DataRequired()])

    submit = SubmitField('Post')