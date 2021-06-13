from . import db
from datetime import datetime

class Pitch(db.Model):
  '''
  Defines arguments for pitch instances
  '''
  __tablename__='pitches'
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(255))
  category = db.Column(db.String(255))
  content = db.Column(db.String(255))
  datePosted = db.Column(db.DateTime,default=datetime.utcnow)
  votes = db.Column(db.Integer, db.ForeignKey('votes.id'))
  postedBy = db.Column(db.Integer, db.ForeignKey('users.id'))
  users = db.relationship('User', backref='users', lazy='dynamic')
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

class User(db.Model):
  '''
  Class that defines arguments for user instances and stores them in users table
  '''
  __tablename__='users'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255))
  userBio = db.Column(db.String(255))
  photo_path = db.Column(db.String(255))
  pitchesCreated = db.Column(db.Integer, db.ForeignKey('pitches.id'))
  password_hash = db.Column(db.String())
  email = db.Column(db.String(), unique = True, index = True)
  pitches = db.relationship('Pitch', backref='pitches', lazy='dynamic')
  comments = db.relationship('Comment', backref = 'comments', lazy = 'dynamic')
  votes = db.relationship('Vote', backref = 'votes', lazy = 'dynamic')
  roleId = db.Column(db.Integer, db.ForeignKey('roles.id'))

  def save(self):
    db.session.add()
    db.session.commit()


class Role(db.Model):
  '''
  Defines arguments for roles intances
  '''
  __tablename__='roles'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255))
  users = db.relationship('User', backref='role', lazy='dynamic')