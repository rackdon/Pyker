# coding=UTF-8
import unittest

from ..classes.hand import Hand
from ..classes.card import Card


class Hand_test(unittest.TestCase):

    def test_have_pair(self):
        mock_hand = [Card('As', 'Corazones'),
                     Card('As', 'Diamantes'),
                     Card('Dos', 'Picas'),
                     Card('Tres', 'Corazones'),
                     Card('Cuatro', 'Diamantes')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.have_group(2), 1)
        self.assertEqual(hand.get_result(7),
                         [7, [1], 'Pair of As'])

    def test_have_double_pair(self):
        mock_hand = [Card('As', 'Corazones'),
                     Card('As', 'Diamantes'),
                     Card('Dos', 'Picas'),
                     Card('Dos', 'Diamantes'),
                     Card('Tres', 'Corazones')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.have_double_pair(), [1, 2])
        self.assertEqual(hand.get_result(6),
                         [6, [1, 2], "Double Pair with As and Dos"])

    def test_hand_with_three_pairs(self):
        mock_hand = [Card('As', 'Corazones'),
                     Card('As', 'Diamantes'),
                     Card('Dos', 'Picas'),
                     Card('Dos', 'Diamantes'),
                     Card('Tres', 'Corazones'),
                     Card('Tres', 'Diamantes')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.have_double_pair(), [1, 3])
        self.assertEqual(hand.get_result(6),
                         [6, [1, 3], "Double Pair with As and Tres"])

    def test_have_two_three(self):
        mock_hand = [Card('Dos', 'Corazones'),
                     Card('Dos', 'Diamantes'),
                     Card('Dos', 'Picas'),
                     Card('Tres', 'Diamantes'),
                     Card('Tres', 'Corazones'),
                     Card('Tres', 'Picas')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.have_group(3), 3)
        self.assertEqual(hand.get_result(5),
                         [5, [3], "Three of Tres"])

    def test_have_three(self):
        mock_hand = [Card('As', 'Corazones'),
                     Card('As', 'Diamantes'),
                     Card('As', 'Picas'),
                     Card('Dos', 'Diamantes'),
                     Card('Tres', 'Corazones')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.have_group(3), 1)
        self.assertEqual(hand.get_result(5),
                         [5, [1], "Three of As"])

    def test_have_four(self):
        mock_hand = [Card('As', 'Corazones'),
                     Card('As', 'Diamantes'),
                     Card('As', 'Picas'),
                     Card('As', 'Tréboles'),
                     Card('Tres', 'Corazones')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.have_group(4), 1)
        self.assertEqual(hand.get_result(4),
                         [4, [1], "Four of As"])

    def test_have_flush(self):
        mock_hand = [Card('As', 'Picas'),
                     Card('As', 'Corazones'),
                     Card('Dos', 'Corazones'),
                     Card('Tres', 'Corazones'),
                     Card('Cuatro', 'Corazones'),
                     Card('Cinco', 'Corazones')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.have_flush(), 'Corazones')
        self.assertEqual(hand.get_result(3),
                         [3, [], "Flush of Corazones"])

    def test_have_straight_with_As_at_the_begining(self):
        mock_hand = [Card('As', 'Corazones'),
                     Card('Dos', 'Corazones'),
                     Card('Rey', 'Picas'),
                     Card('Tres', 'Corazones'),
                     Card('Siete', 'Picas'),
                     Card('Cuatro', 'Corazones'),
                     Card('Cinco', 'Corazones'),
                     Card('Seis', 'Picas')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.have_straight(), 7)
        self.assertEqual(hand.get_result(2),
                         [2, [7], "Straight from Tres to Siete"])

    def test_have_straight_with_As_at_the_end(self):
        mock_hand = [Card('As', 'Corazones'),
                     Card('Dos', 'Picas'),
                     Card('Nueve', 'Tréboles'),
                     Card('Diez', 'Corazones'),
                     Card('Jota', 'Corazones'),
                     Card('Reina', 'Corazones'),
                     Card('Rey', 'Corazones')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.have_straight(), 14)
        self.assertEqual(hand.get_result(2),
                         [2, [14], "Straight from Diez to As"])

    def test_not_have_straight(self):
        mock_hand = [Card('Siete', 'Corazones'),
                     Card('Ocho', 'Corazones'),
                     Card('Nueve', 'Corazones'),
                     Card('Diez', 'Corazones'),
                     Card('Diez', 'Picas'),
                     Card('Diez', 'Tréboles'),
                     Card('Rey', 'Corazones')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.have_straight(), 0)
        self.assertEqual(hand.get_result(2), [2])

    def test_have_full(self):
        mock_hand = [Card('As', 'Corazones'),
                     Card('As', 'Diamantes'),
                     Card('As', 'Picas'),
                     Card('Dos', 'Diamantes'),
                     Card('Dos', 'Corazones')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.have_full(), [1, 2])
        self.assertEqual(hand.get_result(1),
                         [1, [1, 2], "Full with Three of As and Pair of Dos"])

    def test_get_numbers_in_hand(self):
        # This function test get_numbers_in_hand() and
        # order_hand()
        mock_hand = [Card('Tres', 'Corazones'),
                     Card('As', 'Diamantes'),
                     Card('Dos', 'Picas'),
                     Card('As', 'Corazones'),
                     Card('Cuatro', 'Diamantes')]
        hand = Hand(mock_hand)
        self.assertItemsEqual(hand.numbers_in_hand, [1, 1, 2, 3, 4])

    def test_print_hand(self):
        mock_hand = [Card('Rey', 'Corazones'),
                     Card('As', 'Diamantes'),
                     Card('Siete', 'Picas'),
                     Card('Tres', 'Corazones'),
                     Card('Cuatro', 'Diamantes')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.print_hand(), None)

    def test_get_face(self):
        hand = Hand([])
        self.assertEqual(hand.get_face(1), "As")

    def test_get_face_number(self):
        hand = Hand([])
        self.assertEqual(hand.get_face_number("Siete"), 7)

    def test_get_result(self):
        mock_hand = [Card('As', 'Corazones'),
                     Card('As', 'Diamantes'),
                     Card('Dos', 'Picas'),
                     Card('Dos', 'Diamantes'),
                     Card('Tres', 'Corazones')]
        hand = Hand(mock_hand)
        self.assertEqual(hand.determinate_hand(),
                         [6, [1, 2], "Double Pair with As and Dos"])


if __name__ == '__main__':
    unittest.main()
