from flask import render_template, abort, redirect, url_for, request, url_for
from flask_login import login_required
from . import main
from ..models import User, UserProfile, PitchCategory, Pitch, Vote
from .forms import AddCategory, AddPitch, UpdateProfile
from .. import db, photos
from flask_wtf import form

@main.route('/')
def index():
  pitchcategory1 = (PitchCategory.query.filter_by(id = 1).first()).category
  pitchcategory2 = (PitchCategory.query.filter_by(id = 2).first()).category
  pitchcategory3 = (PitchCategory.query.filter_by(id = 3).first()).category
  pitchcategory4 = (PitchCategory.query.filter_by(id = 4).first()).category
  pitchcategory5 = (PitchCategory.query.filter_by(id = 5).first()).category
  pitchcategory6 = (PitchCategory.query.filter_by(id = 6).first()).category
  pitchcategory7 = (PitchCategory.query.filter_by(id = 7).first()).category
  pitchcategory8 = (PitchCategory.query.filter_by(id = 8).first()).category

  return render_template('index.html',pitchcategory1=pitchcategory1,pitchcategory2=pitchcategory2,pitchcategory3=pitchcategory3,pitchcategory4=pitchcategory4,pitchcategory5=pitchcategory5,pitchcategory6=pitchcategory6
  ,pitchcategory7=pitchcategory7,pitchcategory8=pitchcategory8)

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
  user_prof = UserProfile.query.filter_by(userId = user_id).first()

  if user is None:
    abort(404)

  user_prof = user_prof
  pitches = Pitch.query.filter_by(postedBy = user_id).all()

  pitch = pitches

  @main.route('/user/<sname>/update_pic')
  @login_required
  def update_photo(sname):
    user = User.query.filter_by(username = sname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',sname=sname))
  
  return render_template('userinfo.html', user = user, user_prof = user_prof, pitch = pitch, form = form)

@main.route('/user/<sname>/update', methods =['GET','POST'])
def update_info(sname):
  user = User.query.filter_by(name = sname).first()
  if user is None:
    abort(404)

  form = UpdateProfile()
  if form.validate_on_submit():
    profile = UserProfile(userBio = form.bio.data, userId = user.id)

    db.session.add(profile)
    db.session.commit()

    return redirect(url_for('main.user_profile', sname=user.name))
  
  return render_template('updateinfo.html', form = form)

@main.route('/pitches/<category>', methods = ['GET'])
def view_category(category):
  pitch = PitchCategory.query.filter_by(category = category).first()
  pitch_id = pitch.id
  pitches = Pitch.query.filter_by(category = pitch_id).all()

  return render_template('pitchescategorized.html', pitches = pitches)


@main.route('/categoriesadd', methods= ['GET', 'POST'])
def addCat():
  form = AddCategory()
  if form.validate_on_submit():
    categ = PitchCategory(category = form.title.data)

    db.session.add(categ)
    db.session.commit()
    return redirect(url_for('main.addCat'))
  return render_template('addcat.html', form =form)