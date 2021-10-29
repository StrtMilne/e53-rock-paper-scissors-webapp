from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game

@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route("/<one_choice>/<two_choice>")
def played(one_choice, two_choice):
    player_1 = Player("Player 1", one_choice)
    player_2 = Player("Player 2", two_choice)
    winner_object = Game.winner_is(player_1, player_2)
    return render_template("played.html", title="You played a game!", one_choice=one_choice, two_choice=two_choice, winner=winner_object)