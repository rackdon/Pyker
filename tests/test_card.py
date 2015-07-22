import unittest

from classes.card import Card


class Card_test(unittest.TestCase):

    def test_passed_one_card_create_a_string(self):
        card = Card('Cuatro', 'Picas')
        self.assertEqual(card.toString(), 'Cuatro of Picas')

    def test_face_assignment(self):
        card = Card('As', 'Corazones')
        self.assertEqual(card.face, 'As')

    def test_suit_assignment(self):
        card = Card('Dos', 'Picas')
        self.assertEqual(card.suit, 'Picas')


if __name__ == '__main__':
    unittest.main()
