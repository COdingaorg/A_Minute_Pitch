from flask import render_template, redirect, url_for, request, flash  
from flask_login.utils import login_user, logout_user, login_required
from . import auth
from .forms import SignupForm, LoginForm
from ..models import User
from .. import db

@auth.route('/login')
def login():
  return render_template('auth/login.html')

@auth.route('/register', methods = ['GET', 'POST'])
def register():
  form = SignupForm()
  if form.validate_on_submit():
    user = User(name = form.username.data, email = form.email.data, password_hash = form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))
  title = "Create account"
  return render_template('auth/register.html', signupForm = form, title = title)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
  login_form = LoginForm()
  if login_form.validate_on_submit():
    user = User.query.filter_by(email = login_form.email.data).first()
    if user is not None and User.verify_password(login_form.password.data):
      login_user(user, login_form.remember.data)
      return redirect(request.args.get('next') or url_for('main.index'))
    
    flash('invalid username or password')
  title = 'Login'
  return render_template('auth/login.html', login_form = login_form, title = title)

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))
