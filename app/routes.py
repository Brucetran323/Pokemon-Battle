from app import app
from flask import render_template, request, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user
from .pokemon.getpoke import findpokemon
from .forms import SignUpForm, LoginForm, findPoke
from .models import Trainer, Pokemon 
import random

@app.route('/')
def homePage():
    form = findPoke()
    return render_template('index.html')

@app.route('/random')
def randomPokemon():
    random_numbers = []
    pokemon_list = []
    for n in range(5):
        random_numbers.append(random.randint(1,1001))
    for i in random_numbers:
        poke_db = Pokemon.query.filter_by(id=i).first()
        pokemon_list.append(poke_db)
    return render_template('rando_pokemon.html', pokemon1=pokemon_list[0], pokemon2=pokemon_list[1], pokemon3=pokemon_list[2], 
                           pokemon4=pokemon_list[3], pokemon5=pokemon_list[4])


#Add a button to nav bar if you want to use this function, this function is used to add all the pokemon to the database
#Add this to navbar! 
#<li class="nav-item"><a class="nav-link active text-danger" aria-current="page" href="/send-it">Send it</a></li>
@app.route('/send-it')
def sendIt():
    pokeboi =[]
    count = 0
    for i in range(501, 1001):
        poke = findpokemon(i)
        pokemon = Pokemon(picture=poke['Front Shiny'], pokemon_name=poke['Name'], poke_id=poke['Id'] , ability=poke['Ability'],
                base_hp=poke['Base HP'], base_attack=poke['Base ATK'], base_defense=poke['Base DEF'])
        pokemon.savePokemon()
        count = count+1
        print(count)
    return redirect(url_for('homePage'))


