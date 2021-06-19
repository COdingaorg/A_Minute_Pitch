import os
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.models import Comment, Pitch, User, Vote, PitchCategory

#creating app instance
app = create_app('production')
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
  return dict(app = app, db = db, User = User, Pitch = Pitch, Vote = Vote, Comment = Comment, PitchCategory = PitchCategory)

if __name__=='__main__':
  manager.run()
