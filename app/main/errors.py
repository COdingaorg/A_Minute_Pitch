from flask import render_template
from . import main

@main.app_errorhandler(404)
def fourofour(error):
  '''
  function to render 404 page
  '''
  title = '404- Not FOund. Sorry, The page is not avalable'
  return render_template('fourofour.html', title = title),404