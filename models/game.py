from models.player import Player
from random import choice

class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
    
    def winner_is(player_1, player_2):
        player_1_choice = player_1.choice.lower()
        player_2_choice = player_2.choice.lower()

        if player_1_choice == player_2_choice:
            return "None"
        elif player_1_choice == "rock":
            if player_2_choice == "scissors":
                return player_1
            else:
                return player_2
        elif player_1_choice == "paper":
            if player_2_choice == "rock":
                return player_1
            else:
                return player_2
        else:
            if player_2_choice == "paper":
                return player_1
            else:
                return player_2

    def create_player():
        list = ["rock", "paper", "scissors"]
        pick = choice(list)
        return Player("computer", pick)
