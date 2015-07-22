import unittest

from classes.deck_of_cards import Deck_of_cards
from classes.players import Players


class test_players(unittest.TestCase):
    def test_init(self):
        players = Players(Deck_of_cards())
        self.assertIsInstance(players.deck_of_cards, Deck_of_cards)
        self.assertDictEqual(players.players, {})

    def test_add_player(self):
        players = Players(Deck_of_cards())
        players.add_player('Pepe')
        self.assertTrue('Pepe' in players.players)

    def test_remove_player(self):
        players = Players(Deck_of_cards())
        players.add_player('Pepe')
        players.remove_player('Pepe')
        self.assertDictEqual(players.players, {})

if __name__ == '__main__':
    unittest.main()
