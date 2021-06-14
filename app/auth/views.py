from flask import render_template, redirect, url_for
from . import auth
from .forms import SignupForm
from ..models import User
from .. import db

@auth.route('/login')
def login():
  return render_template('auth/login.html')

@auth.route('/register')
def register():
  form = SignupForm
  if form.validate_on_submit():
    user = User(name = form.username.data, email = form.email.data, password_hash = form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))
  title = "Create account"
  return render_template('auth/register.html', signupForm = form, title = title)