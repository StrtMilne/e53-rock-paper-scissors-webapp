from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game

@app.route("/<one_choice>/<two_choice>")
def index(one_choice, two_choice):
    player_1 = Player("Player 1", one_choice)
    player_2 = Player("Player 2", two_choice)
    winner_object = Game.winner_is(player_1, player_2)
    return render_template("played.html", title="Home", one_choice=one_choice, two_choice=two_choice, winner=winner_object)