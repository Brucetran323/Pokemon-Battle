import random
a=[]
for j in range(5):
    a.append(random.randint(1,1015))
print('Randomised list is: ',a)


# FLASK_APP = app
# FLASK_DEBUG = 1 
# SECRET_KEY = testing1234
# SQLALCHEMY_DATABASE_URI = postgresql://cifawulo:2NaQO1XOgiOMj5jw9Pf-NaR_Ng6p35kR@fanny.db.elephantsql.com/cifawulo

# @app.route('/random')
# def randomPokemon():
#     form = findPoke()
#     random_number=(random.randint(0,1020))
#     print(random_number)
#     poke = Pokemon.query.filter_by(poke_id=random_number).first()
#     if poke:
#         print("from DB")
#         poke_info = Pokemon.query.filter_by()
#         return render_template('pokemon.html', pokemon=poke, form=form)
#     else:
#         poke = findpokemon(random_number)
#         print("API called!")
#         if poke:
#             pokemon = Pokemon(picture=poke['Front Shiny'], pokemon_name=poke['Name'], poke_id=poke['Id'] , ability=poke['Ability'],
#                             base_hp=poke['Base HP'], base_attack=poke['Base ATK'], base_defense=poke['Base DEF'])
#             pokemon.savePokemon()
#             print("saved to DB!")
#             return render_template('pokemon.html', pokemon=poke, form=form)
#         else:
#             return render_template('no-pokemon.html', form = form)
