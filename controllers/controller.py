from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game

@app.route("/home")
def index():
    return render_template("index.html", title="Home")

@app.route("/home/<one_choice>/<two_choice>")
def played(one_choice, two_choice):
    player_1 = Player("Player 1", one_choice)
    player_2 = Player("Player 2", two_choice)
    name_1 = player_1.name
    name_2 = player_2.name
    winner_object = Game.winner_is(player_1, player_2)
    return render_template("played.html", title="You played a game!", name_1=name_1, name_2=name_2, one_choice=one_choice, two_choice=two_choice, winner=winner_object)

@app.route("/play")
def computer_game():
    return render_template("play.html", title="Play the computer!")
    
@app.route("/play", methods=["POST"])
def play_computer():
    pick = request.form["choice"]
    player_1 = Player("Player 1", pick)
    player_2 = Game.create_player()
    player_2_choice = player_2.choice
    name_1 = player_1.name
    name_2 = player_2.name
    winner_object = Game.winner_is(player_1, player_2)
    return render_template("played.html", title="You played the computer!", name_1=name_1, name_2=name_2, one_choice=pick, two_choice=player_2_choice, winner=winner_object)
