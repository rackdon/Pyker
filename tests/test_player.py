# coding=UTF-8
import unittest

from ..classes.player import Player
from ..classes.deck_of_cards import Deck_of_cards
from ..classes.card import Card
from ..classes.hand import Hand


class Player_test(unittest.TestCase):
    def test_self_hand(self):
        player = Player(Deck_of_cards(), 'Pepe')
        self.assertEqual(len(player.hand.hand), 5)

    def test_get_result_of_hand(self):
        mock_hand = [Card('As', 'Corazones'),
                     Card('As', 'Diamantes'),
                     Card('As', 'Espadas'),
                     Card('As', 'Tréboles'),
                     Card('Tres', 'Corazones')]
        player = Player(Deck_of_cards(), 'Pepe')
        player.hand = Hand(mock_hand)
        self.assertEqual(player.get_result_of_hand(),
                         [4, [1], 'Four of As', 'Pepe'])

if __name__ == '__main__':
    unittest.main()
