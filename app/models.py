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

class Comment(db.Model):
  '''
  Defines arguments for pitch comments instances and stores them in database
  '''
  __tablename__='comments'
  id = db.Column(db.Integer, primary_key = True)
  content = db.Column(db.String(255))
  postedBy = db.Column(db.String(255), ForeignKey('users.id'))
  datePosted = db.Column(db.DateTime, default = datetime.utcnow)

