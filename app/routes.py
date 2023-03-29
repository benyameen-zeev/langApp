from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.forms import LoginForm, SignupForm
from app.models import User
from app.google_auth import google_blueprint

bp = Blueprint('routes', __name__)

@bp.route('/')
@bp.route('/home')
@login_required
def home():
    return "Hello, " + current_user.email

@bp.route('/email_login', methods=['GET', 'POST'])
def email_login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('routes.home'))
        else:
            flash('Invalid email or password')
    return render_template('email_login.html', form=form)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))

    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful')
        return redirect(url_for('routes.email_login'))
    return render_template('signup.html', form=form)

@bp.route('/google/login')
def google_login():
    return redirect(url_for('google.login'))

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.home'))

@google_blueprint.session_created
def session_created(session):
    user_email = session.get('email')
    user = User.query.filter_by(email=user_email).first()
    if not user:
        user = User(email=user_email)
        db.session.add(user)
        db.session.commit()
    login_user(user)
    return redirect(url_for('routes.home'))

@google_blueprint.session_destroyed
def session_destroyed(session):
    return redirect(url_for('routes.home'))
