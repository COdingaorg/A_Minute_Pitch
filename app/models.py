class Pitch(db.Model):
  '''
  Defines arguments for pitch instances
  '''
  __tablename__='pitches'
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(255))
  category = db.Column(db.String(255))
  content = db.Column(db.String(255))
  datePosted = db.Column(db.DateTime, default = datetime.utcnow)
  votes = db.Column(db.Integer, db.ForeignKey('votes.id'))
  postedBy = db.Column(db.String, db.ForeignKey('users.id'))

