from ..models import Trainer, Pokemon, teams
from ..forms import SignUpForm, LoginForm, findPoke
from .getpoke import findpokemon
from flask_login import current_user, login_user, logout_user, login_required
from flask import Blueprint, render_template, request, redirect, url_for, flash
pokemon = Blueprint('pokemon', __name__, template_folder='pokemon_templates')


@pokemon.route('/catch-em/<int:p_id>')
def catchPokemon(p_id):
    find_poke_in_api = findpokemon(p_id)
    pokemon = Pokemon(picture=find_poke_in_api['Front Shiny'], pokemon_name=find_poke_in_api['Name'], poke_id=find_poke_in_api['Id'], ability=find_poke_in_api['Ability'],
                      base_hp=find_poke_in_api['Base HP'], base_attack=find_poke_in_api['Base ATK'], base_defense=find_poke_in_api['Base DEF'])
    pokemon.savePokemon()

    return render_template('catch-me.html', pokemon1=p_id)


~~~~{'product_name': 'DANVOUY Womens T Shirt Casual Cotton Short', 'price': 12.99, 
     'description': '95%Cotton,5%Spandex, Features: Casual, Short Sleeve, Letter Print,V-Neck,Fashion Tees, The fabric is soft and has some stretch., Occasion: Casual/Office/Beach/School/Home/Street. Season: Spring,Summer,Autumn,Winter.', 
     'category': "women's clothing", 'product_image': 'https://fakestoreapi.com/img/61pHAEJ4NML._AC_UX679_.jpg'}