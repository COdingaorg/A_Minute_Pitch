from flask_wtf.form import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import Required



class UpdateProfile(FlaskForm):
  '''
  creates form for updating user profile
  '''
  photo = StringField(' ')
  bio = StringField('How do you explain yourself: ', validators=[Required()])
  submit = SubmitField('submit')

