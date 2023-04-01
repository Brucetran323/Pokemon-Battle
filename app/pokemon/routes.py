from flask import Blueprint, render_template, request, redirect, url_for, flash
pokemon = Blueprint('pokemon', __name__, template_folder='pokemon_templates')
from flask_login import current_user, login_user, logout_user, login_required
from .getpoke import findpokemon
from ..forms import SignUpForm, LoginForm, findPoke
from ..models import Trainer, Pokemon, teams

@pokemon.route('/catch-em/<p_img>/<int:p_id>')
def catchPokemon(p_img,p_id):
    return render_template('catch-me.html', pokemon1 = p_id, pokemon2 = p_img)


