from ..models import Trainer, Pokemon, teams
from ..forms import SignUpForm, LoginForm, findPoke
from .getpoke import findpokemon
from flask_login import current_user, login_user, logout_user, login_required
from flask import Blueprint, render_template, request, redirect, url_for, flash
pokemon = Blueprint('pokemon', __name__, template_folder='pokemon_templates')


@pokemon.route('/catch-em/<int:p_id>')
def catchPokemon(p_id):
    current_user_poke_count = len(current_user.caught.all())
    if current_user_poke_count >= 5:
        print("NO!!!!")
        return redirect(url_for('homePage'))
    else:
        poke = Pokemon.query.filter_by(poke_id=p_id).first()
        flash(f"{poke} has been caught!")
        current_user.catchPokemon(poke)
        pokemon_info = Pokemon.query.filter_by(poke_id=p_id).first()
        print(pokemon_info)
        return render_template('catch-me.html', pokemon = pokemon_info)
    
