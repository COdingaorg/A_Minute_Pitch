from sqlalchemy.orm import backref, lazyload
from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class Pitch(db.Model):
  '''
  Defines arguments for pitch instances
  '''
  __tablename__='pitches'
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(255))
  category = db.Column(db.Integer, db.ForeignKey('categories.id'))
  content = db.Column(db.String(255))
  datePosted = db.Column(db.DateTime,default=datetime.utcnow)
  votes = db.Column(db.Integer, db.ForeignKey('votes.id'))
  postedBy = db.Column(db.Integer, db.ForeignKey('users.id'))
  users = db.relationship('User', backref=backref('users', lazy='dynamic'))
  comments = db.relationship('Comment', backref = 'comments', lazy = 'dynamic')

class Comment(db.Model):
  '''
  Defines arguments for pitch comments instances and stores them in database
  '''
  __tablename__='comments'
  id = db.Column(db.Integer, primary_key = True)
  content = db.Column(db.String(255))
  postedBy = db.Column(db.Integer, db.ForeignKey('users.id'))
  datePosted = db.Column(db.DateTime,default=datetime.utcnow)
  pitchId = db.Column(db.Integer, db.ForeignKey('pitches.id'))

class Vote(db.Model):
  '''
  Defines arguments for vote instances and stores them in votes table
  '''
  __tablename__='votes'
  id = db.Column(db.Integer, primary_key = True)
  voteCount = db.Column(db.Integer)
  voter = db.Column(db.Integer, db.ForeignKey('users.id'))
  pitches = db.relationship('Pitch', backref = 'pitches', lazy='dynamic')

class User(UserMixin ,db.Model):
  '''
  Class that defines arguments for user instances and stores them in users table
  '''
  __tablename__='users'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255))
  password_hash = db.Column(db.String())
  email = db.Column(db.String(), unique = True, index = True)
  profile = db.relationship('UserProfile', backref = 'profile', lazy = 'dynamic')
  pitchesAdded = db.relationship('Pitch', backref='pitchesAdded', lazy='dynamic')
  commentsAdded = db.relationship('Comment', backref = 'commentsAdded', lazy = 'dynamic')
  votesAdded = db.relationship('Vote', backref = 'votesAdded', lazy = 'dynamic')

  @property
  def password(self):
    raise AttributeError('You cannot view password')

  @password.setter
  def password(self, password):
    self.password_hash = (password)

  def verify_password(self, password):
    return (self.password_hash, password)


class UserProfile(db.Model):
  '''
  Defines arguments for photoprofile instances
  '''
  __tablename__= 'profiles'
  id = db.Column(db.Integer, primary_key = True)
  photo_path = db.Column(db.String())
  userBio = db.Column(db.String(255))
  userId = db.Column(db.Integer, db.ForeignKey('users.id'))
  pitchesCreated = db.Column(db.Integer, db.ForeignKey('pitches.id'))

class PitchCategory(db.Model):

  __tablename__ = 'categories'
  id = db.Column(db.Integer, primary_key = True)
  category = db.Column(db.String(100))
  pitchitem = db.relationship('Pitch', backref='pitchitem', lazy='dynamic') 