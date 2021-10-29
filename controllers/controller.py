from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game

@app.route("/<one_choice>/<two_choice")
def index(one_choice, two_choice):
    player_1 = Player("player_1", one_choice)
    player_2 = Player("player_2", two_choice)
    winner = Game(player_1, player_2)
    return render_template("index.html", title="Home", one_choice=one_choice, two_choice=two_choice, winner=winner)