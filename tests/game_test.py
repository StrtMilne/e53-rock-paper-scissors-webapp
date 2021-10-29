import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):

    def test_rock_v_scissors(self):
        player_1 = Player("John", "rock")
        player_2 = Player("Paul", "scissors")
        self.assertEqual(player_1, Game.winner_is(player_1, player_2))

    def test_rock_v_rock(self):
        player_1 = Player("John", "rock")
        player_2 = Player("Paul", "rock")
        self.assertEqual("None", Game.winner_is(player_1, player_2))

    def test_rock_v_paper(self):
        player_1 = Player("John", "rock")
        player_2 = Player("Paul", "paper")
        self.assertEqual(player_2, Game.winner_is(player_1, player_2))
    
    def test_paper_v_scissors(self):
        player_1 = Player("John", "paper")
        player_2 = Player("Paul", "scissors")
        self.assertEqual(player_2, Game.winner_is(player_1, player_2))

    def test_paper_v_rock(self):
        player_1 = Player("John", "paper")
        player_2 = Player("Paul", "rock")
        self.assertEqual(player_1, Game.winner_is(player_1, player_2))

    def test_paper_v_paper(self):
        player_1 = Player("John", "paper")
        player_2 = Player("Paul", "paper")
        self.assertEqual("None", Game.winner_is(player_1, player_2))
    
    def test_scissors_v_scissors(self):
        player_1 = Player("John", "scissors")
        player_2 = Player("Paul", "scissors")
        self.assertEqual("None", Game.winner_is(player_1, player_2))

    def test_scissors_v_rock(self):
        player_1 = Player("John", "scissors")
        player_2 = Player("Paul", "rock")
        self.assertEqual(player_2, Game.winner_is(player_1, player_2))

    def test_scissors_v_paper(self):
        player_1 = Player("John", "scissors")
        player_2 = Player("Paul", "paper")
        self.assertEqual(player_1, Game.winner_is(player_1, player_2))

    
    