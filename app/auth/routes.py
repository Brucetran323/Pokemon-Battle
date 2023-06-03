from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
auth = Blueprint('auth', __name__, template_folder='auth_templates')
from flask_login import current_user, login_user, logout_user
from ..forms import SignUpForm, LoginForm
from ..models import Trainer


@auth.route('/login', methods=['GET', 'POST'])
def loginPage():
    form = LoginForm()
    if request.method == "POST":
        if form.validate():
          username = form.username.data
          password = form.password.data
        trainer = Trainer.query.filter_by(username=username).first()
        if trainer:
            if check_password_hash(trainer.password, password):
                login_user(trainer)
                flash(f'Welcome {trainer.trainer_name}!', 'success')
                return redirect (url_for('homePage'))             
            else:
                flash('Username or password incorrect!', 'danger')
        else:
            flash('Username or password incorrect!', 'danger')
    return render_template('login.html', form = form)

@auth.route('/register', methods=['GET', 'POST'])
def registerPage():
    form = SignUpForm()
    if request.method == "POST":
        if form.validate():
            trainer_name = form.trainer_name.data
            username = form.username.data
            password = form.password.data
            if Trainer.query.filter_by(username=username).first():
                flash('That username already exists!', 'danger')
                return redirect(url_for('auth.loginPage'))
            trainer = Trainer(trainer_name, username, password)
            trainer.saveTrainer()
            flash(f'Welcome {trainer.trainer_name}! Please login!', 'success')
            return redirect (url_for('auth.loginPage'))
    return render_template('register.html', form=form)


@auth.route('/logout')
def logOut():
    logout_user()
    flash('Logged out!', 'success')
    return redirect (url_for('homePage'))