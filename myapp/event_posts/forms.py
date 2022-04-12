from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Details', validators=[DataRequired()])
    image_url = StringField('Image_Url', validators=[DataRequired()])
    location = TextAreaField('Location', validators=[DataRequired()])
    eventdate = StringField('Eventdate', validators=[DataRequired()])
    # image = StringField('Image', validators=[DataRequired()])
    # attending = BooleanField('Attending', validators=[DataRequired()])
    # favorite = BooleanField('Attending', validators=[DataRequired()])

    submit = SubmitField('Post')