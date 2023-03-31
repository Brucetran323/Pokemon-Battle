from app import app
from flask import render_template, request, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user
from .pokemon.getpoke import findpokemon
from .forms import SignUpForm, LoginForm, findPoke
from .models import Trainer, Pokemon 
import random

@app.route('/random')
def randomPokemon():
    form = findPoke()
    random_list=[]
    for n in range(5):
        random_list.append(random.randint(1,1015))
        for i in random_list:
            poke_stuff=[]
            poke = findpokemon(i)
            poke_stuff.append(poke)
    print(poke_stuff)
            
    print("API BBY")
    return render_template('pokemon.html', pokemon=poke, form=form)






@app.route('/')
def homePage():
    form = findPoke()
    return render_template('index.html', form = form)
