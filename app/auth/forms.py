from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Required, EqualTo
from ..models import User

class SignupForm(FlaskForm):
  username = StringField('Your Name: ', validators=[Required()])
  email = StringField('Email Address: ', validators=[Required(), Email()])
  password = PasswordField('Create password: ', validators=[Required(), EqualTo('password_confirm', message='Passwords must be the same')])
  password_confirm = PasswordField('Repeat Password: ', validators=[Required()])
  signup = SubmitField('signup')