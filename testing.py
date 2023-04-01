import random
import requests, json

def findpokemon(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = requests.get(url)
    if response.ok:
        my_dict = response.json()
        pokemon_dict = {}
        pokemon_dict["Name"] = my_dict["name"]
        return pokemon_dict
    else:
        return None
    

random_list=[]
poke_stuff=[]

for n in range(5):
    random_list.append(random.randint(1,1015))
for i in random_list:
    poke = findpokemon(i)
    poke_stuff.append(poke)

p1 = poke_stuff[0]
p2 = poke_stuff[1]
p3 = poke_stuff[2]
p4 = poke_stuff[3]
p5 = poke_stuff[4]  
print(poke_stuff) 






@app.route('/random')
def randomPokemon():
    form = findPoke()
    random_number=(random.randint(0,1020))
    print(random_number)
    poke = Pokemon.query.filter_by(poke_id=random_number).first()
    if poke:
        print("from DB")
        poke_info = Pokemon.query.filter_by()
        return render_template('pokemon.html', pokemon=poke, form=form)
    else:
        poke = findpokemon(random_number)
        print("API called!")
        if poke:
            pokemon = Pokemon(picture=poke['Front Shiny'], pokemon_name=poke['Name'], poke_id=poke['Id'] , ability=poke['Ability'],
                            base_hp=poke['Base HP'], base_attack=poke['Base ATK'], base_defense=poke['Base DEF'])
            pokemon.savePokemon()
            print("saved to DB!")
            return render_template('pokemon.html', pokemon=poke, form=form)
        else:
            return render_template('no-pokemon.html', form = form)




