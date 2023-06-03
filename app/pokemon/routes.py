from ..models import Trainer, Pokemon, teams, db
from ..forms import SignUpForm, LoginForm, findPoke
from .getpoke import findpokemon
from flask_login import current_user
from flask import Blueprint, render_template, request, redirect, url_for, flash
pokemon = Blueprint('pokemon', __name__, template_folder='pokemon_templates')

@pokemon.route('/view-team/poke/<int:t_id>')
def viewTeamsPoke(t_id):
    trainer = Trainer.query.get(t_id)
    trainer_name = trainer.trainer_name
    pokemon_list = trainer.caught.all()
    if pokemon_list:
        return render_template('view_team_poke.html', pokemon1=pokemon_list[0], pokemon2=pokemon_list[1], pokemon3=pokemon_list[2], 
                                pokemon4=pokemon_list[3], pokemon5=pokemon_list[4], trainer_id=t_id, trainer_name=trainer_name)
    else:
        flash('This trainer currently has no pokemon!', 'danger')
        return redirect(url_for('pokemon.Teams'))

@pokemon.route('/teams')
def Teams():
    teams =  Trainer.query.all()
    teams.remove(current_user)
    return render_template('teams.html', teams=teams)

@pokemon.route('/rankings')
def leaderBoard():
    trainers = Trainer.query.all()
    trainers.remove(current_user)
    return render_template('leaderboard.html', trainers=trainers)

@pokemon.route('/my-pokemon')
def showMyPokemon():
    pokemon_list = current_user.caught.all()
    count = len(pokemon_list)
    if count == 5:
        return render_template('my-pokemon.html', pokemon1=pokemon_list[0], pokemon2=pokemon_list[1], pokemon3=pokemon_list[2], 
                            pokemon4=pokemon_list[3], pokemon5=pokemon_list[4], count=count)
    else:
        flash("You currently do not have a team! Please catch a team", 'danger')
        return redirect(url_for('randomPokemon'))

@pokemon.route('/catch-em-all/<int:p1>/<int:p2>/<int:p3>/<int:p4>/<int:p5>/')
def catchAll(p1,p2,p3,p4,p5):
    poke_list = [p1,p2,p3,p4,p5]
    print(poke_list)
    current_user.caught = []
    db.session.commit()
    for p in poke_list:
        poke_db = Pokemon.query.filter_by(id=p).first()
        current_user.catchPokemon(poke_db)
    flash('New team caught!', 'success')
    return redirect(url_for('pokemon.showMyPokemon'))
    
@pokemon.route('/release-all')
def releaseAll():
    current_user.caught = []
    db.session.commit()
    return redirect(url_for('pokemon.showMyPokemon'))
    
@pokemon.route('/battle-em')
def battlePokemon():
    current_user_poke_count = len(current_user.caught.all())
    if current_user_poke_count == 5:
        current_user_pokemon = current_user.caught.all()
        p1 = current_user_pokemon[0]
        p2 = current_user_pokemon[1]
        p3 = current_user_pokemon[2]
        p4 = current_user_pokemon[3]
        p5 = current_user_pokemon[4]    
        trainers = Trainer.query.all()
        trainers_able_to_battle = []
        for t in trainers:
            pokemon_caught = len(t.caught.all())
            if pokemon_caught == 5:
                trainers_able_to_battle.append(t)
        return render_template('battle-pokemon.html', p1 = p1, p2 = p2, p3 = p3, p4 = p4, p5 = p5, trainers=trainers_able_to_battle)
    else:
        
        return redirect(url_for('pokemon.showMyPokemon'))
    
@pokemon.route('/final-battle/<int:t_id>')
def FinalBattle(t_id):
    enemy = Trainer.query.get(t_id)
    print(f'{current_user} VS. {enemy}')
    current_user_team = current_user.caught.all()
    enemy_team = enemy.caught.all()
    current_user_attack = 0
    enemy_team_attack = 0
    for a in current_user_team:
        attack = (a.base_attack)
        current_user_attack += attack
    for a in enemy_team:
        attack = (a.base_attack)
        enemy_team_attack += attack
    print(f'CURRENT:{current_user_attack}\nENEMY:{enemy_team_attack}')
    if current_user_attack > enemy_team_attack:
        current_user.winner()
        enemy.loser()
        print('CURRENT USER WIN\nENEMY TEAM LOSE')
        return render_template('battle-winner.html')
    else:
        current_user.loser()
        enemy.winner()
        print('ENEMY TEAM WINNER\nCURRENT USER LOSS')
        return render_template('battle-loser.html')