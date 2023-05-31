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
          print(username, password)
        trainer = Trainer.query.filter_by(username=username).first()
        if trainer:
            print(trainer)
            if check_password_hash(trainer.password, password):
                login_user(trainer)
                flash('This is a flash message', 'success')
                return redirect (url_for('homePage'))             
            else:
                flash('nope!')
        else:
            flash('nope!',category='danger')
    return render_template('login.html', form = form)

@auth.route('/register', methods=['GET', 'POST'])
def registerPage():
    form = SignUpForm()
    if request.method == "POST":
        if form.validate():
            first_name = form.first_name.data
            last_name = form.last_name.data
            username = form.username.data
            email = form.email.data
            password = form.password.data
            if Trainer.query.filter_by(username=username).first():
                flash('That username already exists, please try another!', 'warning')
                return redirect(url_for('auth.loginPage'))
            if Trainer.query.filter_by(email=email).first():
                flash('that email has been used previously, try again', 'warning')
                return redirect(url_for('auth.loginPage'))
            trainer = Trainer(first_name, last_name, username, email, password)
            trainer.saveTrainer()
            return redirect (url_for('auth.loginPage'))
    return render_template('register.html', form=form)


@auth.route('/logout')
def logOut():
    logout_user()
    return redirect (url_for('homePage'))