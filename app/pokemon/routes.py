from flask import Blueprint, render_template, request, redirect, url_for, flash
pokemon = Blueprint('pokemon', __name__, template_folder='pokemon_templates')
from flask_login import current_user, login_user, logout_user, login_required
from .getpoke import findpokemon
from ..forms import SignUpForm, LoginForm, findPoke
from ..models import Trainer, Pokemon, teams

@pokemon.route('/show-pokemon/<int:pokemon_id>')
def showPokemon():
    form = findPoke()
    return render_template('pokemon.html', form = form)

