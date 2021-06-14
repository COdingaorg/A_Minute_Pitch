from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Email, Required, EqualTo, Length
from ..models import User

class SignupForm(FlaskForm):
  username = StringField('Your Name: ', validators=[Required()])
  email = StringField('Email Address: ', validators=[Required(), Email()])
  password = PasswordField('Create password: ', validators=[Length(min=6, max=16),Required(), EqualTo('password_confirm', message='Passwords must be the same')])
  password_confirm = PasswordField('Repeat Password: ', validators=[Required()])
  signup = SubmitField('signup')

  def validate_username(self, data_field):
    if User.query.filter_by(name=data_field.data).first():
      raise ValidationError('username already taken')

  def validate_email(self, data_field):
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError('Email already exists')

class LoginForm(FlaskForm):
  email = StringField('Your Email Address: ', validators=[Required(), Email()])
  password = PasswordField('Enter Password: ', validators=[Required()])
  remember = BooleanField('Remeber Me')
  submit = SubmitField('Log in')