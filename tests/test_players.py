# coding=UTF-8
import unittest

from ..classes.deck_of_cards import Deck_of_cards
from ..classes.players import Players
from ..classes.card import Card
from ..classes.hand import Hand


class Players_test(unittest.TestCase):
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

    def test_who_wins_with_same_kind_of_simple_hand(self):
        player2_hand = [Card('As', 'Corazones'),
                        Card('Dos', 'Corazones'),
                        Card('Tres', 'Picas'),
                        Card('Cuatro', 'Picas'),
                        Card('As', 'Picas')]

        player1_hand = [Card('Diez', 'Picas'),
                        Card('Rey', 'Corazones'),
                        Card('Reina', 'Corazones'),
                        Card('Rey', 'Picas'),
                        Card('Jota', 'Picas')]

        players = Players(Deck_of_cards())
        players.add_player('Pepe')
        players.add_player('Juan')
        player1 = players.players.get('Pepe')
        player1.hand = Hand(player1_hand)
        player2 = players.players.get('Juan')
        player2.hand = Hand(player2_hand)
        self.assertEqual(players.who_wins(), 'Juan wins with Pair of As')

    def test_who_wins_with_same_kind_of_sompound_hand(self):
        player1_hand = [Card('As', 'Corazones'),
                        Card('Tres', 'Corazones'),
                        Card('Tres', 'Picas'),
                        Card('Cuatro', 'Picas'),
                        Card('As', 'Picas')]

        player2_hand = [Card('As', 'Diamantes'),
                        Card('Rey', 'Corazones'),
                        Card('Reina', 'Corazones'),
                        Card('Rey', 'Picas'),
                        Card('As', 'Tréboles')]

        players = Players(Deck_of_cards())
        players.add_player('Pepe')
        players.add_player('Juan')
        player1 = players.players.get('Pepe')
        player1.hand = Hand(player1_hand)
        player2 = players.players.get('Juan')
        player2.hand = Hand(player2_hand)
        self.assertEqual(players.who_wins(),
                         'Juan wins with Double Pair with As and Rey')

    def test_who_wins_with_simple_hand_draw(self):
        player1_hand = [Card('Rey', 'Diamantes'),
                        Card('Dos', 'Corazones'),
                        Card('Tres', 'Picas'),
                        Card('Cuatro', 'Picas'),
                        Card('Rey', 'Picas')]

        player2_hand = [Card('Diez', 'Picas'),
                        Card('Rey', 'Corazones'),
                        Card('Reina', 'Corazones'),
                        Card('Rey', 'Tréboles'),
                        Card('Jota', 'Picas')]

        players = Players(Deck_of_cards())
        players.add_player('Pepe')
        players.add_player('Juan')
        player1 = players.players.get('Pepe')
        player1.hand = Hand(player1_hand)
        player2 = players.players.get('Juan')
        player2.hand = Hand(player2_hand)
        self.assertEqual(players.who_wins(), 'There is a draw')

    def test_who_wins_with_compound_hand_draw(self):
        player1_hand = [Card('Rey', 'Diamantes'),
                        Card('Dos', 'Corazones'),
                        Card('Dos', 'Picas'),
                        Card('Cuatro', 'Picas'),
                        Card('Rey', 'Picas')]

        player2_hand = [Card('Dos', 'Diamantes'),
                        Card('Rey', 'Corazones'),
                        Card('Reina', 'Corazones'),
                        Card('Rey', 'Tréboles'),
                        Card('Dos', 'Tréboles')]

        players = Players(Deck_of_cards())
        players.add_player('Pepe')
        players.add_player('Juan')
        player1 = players.players.get('Pepe')
        player1.hand = Hand(player1_hand)
        player2 = players.players.get('Juan')
        player2.hand = Hand(player2_hand)
        self.assertEqual(players.who_wins(), 'There is a draw')
if __name__ == '__main__':
    unittest.main()
