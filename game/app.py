from flask import Flask, render_template, request, redirect, url_for
from typing import Dict, Type
from functools import wraps

import classes as classes
import equipment as equipment
import utils as utils
from hero import Player, Enemy, Hero
from controller import Game_Singleton


app = Flask(__name__)
app.url_map.strict_slashes = False

heroes: Dict[str, Type[Hero]] = dict()
Equipment: equipment.EquipmentData = utils.load_equipment()

my_game = Game_Singleton()



def game_processing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if my_game.game_processing:
            return func(*args, **kwargs)
        if my_game.game_result:
            return render_template('fight.html', heroes=heroes, result=my_game.game_result)
        return redirect(url_for('index'))
    return wrapper



def render_character_template(*args, **kwargs) -> str:
    return render_template('hero_choosing.html', result={
            "classes": classes.classes.keys(),   
            "weapons": Equipment.weapon_names,    
            "armors": Equipment.armor_names,
            **kwargs,
            },
        )



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/choose-hero/', methods=['GET', 'POST'])
def choose_hero():
    if request.method == 'GET':
        return render_character_template(
            header = 'Choose your hero',      
            button = 'Choose your enemy'  
            )

    heroes["player"] = Player(
        class_ = classes.classes[request.form["unit_class"]],
        weapon = Equipment.get_weapon(request.form["weapon"]),
        armor = Equipment.get_armor(request.form["armor"]),
        name = request.form["name"]
    )

    return redirect(url_for('choose_enemy'))



@app.route('/choose-enemy/', methods=['GET', 'POST'])
def choose_enemy():
    if request.method == 'GET':
        return render_character_template(
            header = 'Choose your enemy',      
            button = 'Start a battle'  
        )

    heroes["enemy"] = Enemy(
        class_ = classes.classes[request.form["unit_class"]],
        weapon = Equipment.get_weapon(request.form["weapon"]),
        armor = Equipment.get_armor(request.form["armor"]),
        name = request.form["name"]
    )

    return redirect(url_for('start_fight'))




@app.route('/fight/start_fight')
def start_fight():
    if 'player' in heroes and 'enemy' in heroes:
        my_game.run(**heroes)
        return render_template('fight.html', heroes=heroes, result="The battle has started")
    
    return redirect(url_for('index'))



@app.route('/fight/hit')
@game_processing
def hit():
    return render_template('fight.html', heroes=heroes, result=my_game.player_hit())



@app.route('/fight/use-skill')
@game_processing
def use_skill():
    return render_template('fight.html', heroes=heroes, result=my_game.player_use_skill())



@app.route('/fight/pass-turn')
@game_processing
def pass_turn():
    return render_template('fight.html', heroes=heroes, result=my_game.next_turn())



@app.route('/fight/end-fight')
def end_fight():
    return redirect(url_for("index"))



if __name__ == '__main__':
    app.run(debug=False)

