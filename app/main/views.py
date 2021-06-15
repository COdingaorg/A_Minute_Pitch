from flask import render_template, abort
from flask_login import login_required
from . import main
from ..models import User, UserProfile

@main.route('/')
def index():
  return render_template('index.html')

@main.route('/minutepitch/pitches')
@login_required
def new_pitch(id):
  pass

@main.route('/user/<sname>')
def user_profile(sname):
  user = User.query.filter_by(name = sname).first()
  user_id = user.id
  user_prof = UserProfile.query.filter_by(userId = user_id)

  if user is None:
    abort(404)
  
  return render_template('info/userinfo.html', user = user, user_prof = user_prof)