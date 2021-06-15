from flask import render_template, abort, redirect, url_for
from flask_login import login_required
from . import main
from ..models import User, UserProfile, PitchCategory, Pitch, Vote
from .forms import AddPitch, UpdateProfile
from .. import db

@main.route('/')
def index():
 pitchcategory1 = (PitchCategory.query.filter_by(id = 10).first()).category
 pitchcategory2 = (PitchCategory.query.filter_by(id = 11).first()).category
 pitchcategory3 = (PitchCategory.query.filter_by(id = 12).first()).category
 pitchcategory4 = (PitchCategory.query.filter_by(id = 13).first()).category
 pitchcategory5 = (PitchCategory.query.filter_by(id = 14).first()).category
 pitchcategory6 = (PitchCategory.query.filter_by(id = 15).first()).category
 pitchcategory7 = (PitchCategory.query.filter_by(id = 16).first()).category
 pitchcategory8 = (PitchCategory.query.filter_by(id = 17).first()).category

 return render_template('index.html', category1 = pitchcategory1, category2 = pitchcategory2,category3 = pitchcategory3,category4 = pitchcategory4,
  category5 = pitchcategory5,category6 = pitchcategory6,category7 = pitchcategory7,category8 = pitchcategory8 )

@main.route('/<sname>/pitches', methods = ['GET','POST'])
@login_required
def new_pitch(sname):
  formAdd = AddPitch()
  if formAdd.validate_on_submit():
    title = formAdd.head.data
    category = PitchCategory.query.filter_by(category = formAdd.cat.data).first()
    content = formAdd.text.data
    user = User.query.filter_by(name = sname).first()

    pitch = Pitch(title=title, category=category.id, content=content, postedBy = user.id)

    db.session.add(pitch)
    db.session.commit()
    return redirect(url_for('main.index'))


  return render_template('addpitch.html', addpitchform = formAdd)


@main.route('/user/<sname>')
def user_profile(sname):
  user = User.query.filter_by(name = sname).first()
  user_id = user.id
  user_prof = UserProfile.query.filter_by(userId = user_id)

  if user is None:
    abort(404)
  
  return render_template('userinfo.html', user = user, user_prof = user_prof)

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

    return redirect(url_for('main.user_profile', sname=user.name))
  
  return render_template('updateinfo.html', form = form)
