from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Details', validators=[DataRequired()])
    image_url = StringField('Image_Url', validators=[DataRequired()])
    location = TextAreaField('Location', validators=[DataRequired()])
    eventdate = StringField('Eventdate', validators=[DataRequired()])
    
    submit = SubmitField('Post')