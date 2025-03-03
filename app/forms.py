from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired(), Email()])
    subject = StringField("Subject", validators=[InputRequired()])
    message = TextAreaField("Message", validators=[InputRequired()])