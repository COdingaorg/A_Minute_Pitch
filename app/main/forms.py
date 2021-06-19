from flask_wtf.form import FlaskForm
from wtforms.fields.core import RadioField, StringField
from wtforms.fields.simple import SubmitField, TextAreaField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
  '''
  creates form for updating user profile
  '''
  bio = StringField('How do you explain yourself: ', validators=[Required()])
  submit = SubmitField('submit')

class AddPitch(FlaskForm):
  '''
  creates form for adding pitch
  '''
  head = StringField('Enter title')
  cat = RadioField('Category: ', choices=[('Pick-up Lines', 'pickuplines category'),('Motivation', 'Motivation category'),('Career', 'Career category'),('Business Ideas', 'Business ideas category'),
  ('Games', 'Games category'),('Interview', 'Interview category')],default='Go wild')
  text = TextAreaField('Describe')
  submit = SubmitField('submit')

class AddCategory(FlaskForm):
  title = StringField('Enter category')
  submit = SubmitField('submit')