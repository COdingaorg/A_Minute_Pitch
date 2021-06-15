from flask import render_template, abort, redirect, url_for
from flask_login import login_required
from . import main
from ..models import User, UserProfile
from .forms import UpdateProfile
from . import db

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

@main.route('/user/<sname>/update', methods =['GET','POST'])
def update_info(sname):
  user = User.query.filter_by(name = sname).first()
  if user is None:
    abort(404)

  form = UpdateProfile()
  if form.validate_on_submit():
    UpdateProfile.userBio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile', sname=user.name))
  
  return render_template('profile.updateinfo.html', form = form)