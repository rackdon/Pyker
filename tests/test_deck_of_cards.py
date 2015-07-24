import unittest
import copy

from ..classes.deck_of_cards import Deck_of_cards
from ..classes.card import Card


class Deck_of_cards_test(unittest.TestCase):

    def test_deck_length_in_init(self):
        deck_of_cards = Deck_of_cards()
        self.assertEqual(len(deck_of_cards.deck), 52)

    def test_shuffle(self):
        deck_of_cards = Deck_of_cards()
        deck_without_shuffle = copy.copy(deck_of_cards.deck)
        deck_of_cards.shuffle()

        def changes_in_deck():
            for i in range(0, len(deck_without_shuffle)):
                if deck_without_shuffle[i] != deck_of_cards.deck[i]:
                    return True
            return False
        self.assertEqual(changes_in_deck(), True)

    def test_deal_hand(self):
        deck_of_cards = Deck_of_cards()
        self.assertEqual(len(deck_of_cards.deal_hand()), 5)

    def test_deal_card(self):
        deck_of_cards = Deck_of_cards()
        self.assertIsInstance(deck_of_cards.deal_card(), Card)

if __name__ == '__main__':
    unittest.main()
