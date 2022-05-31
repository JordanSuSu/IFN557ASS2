from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired

# general basic Login Form


class LogInForm(FlaskForm):
    userName = StringField("Your User Name", validators=[InputRequired()])
    password = StringField("Your Password", validators=[InputRequired()])
    submit = SubmitField("Login")
