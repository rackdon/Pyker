import unittest

from ..classes.results import Results


class Results_test(unittest.TestCase):
    def test_init(self):
        mock_results = [[8, [4], 'Higher Card with Cuatro', 'Pepe'],
                        [8, [7], 'Higher Card with Siete', 'Juan']]
        results = Results(mock_results)
        self.assertEqual(results.results,
                         [[8, [4], 'Higher Card with Cuatro', 'Pepe'],
                          [8, [7], 'Higher Card with Siete', 'Juan']])

    def test_obtain_final_result_no_draw(self):
        mock_results = [[8, [4], 'Higher Card with Cuatro', 'Pepe'],
                        [8, [7], 'Higher Card with Siete', 'Juan']]
        results = Results(mock_results)
        self.assertEqual(results.obtain_final_result(),
                         'Juan wins with Higher Card with Siete')

    def test_obtain_final_result_with_draw(self):
        mock_results = [[8, [4], 'Higher Card with Cuatro', 'Pepe'],
                        [8, [4], 'Higher Card with Cuatro', 'Juan']]
        results = Results(mock_results)
        self.assertEqual(results.obtain_final_result(),
                         'There is a draw between Juan Pepe '
                         + 'with Higher Card with Cuatro')

    def test_is_draw_without_draw(self):
        mock_results = [[8, [4], 'Higher Card with Cuatro', 'Pepe'],
                        [8, [7], 'Higher Card with Siete', 'Juan']]
        results = Results(mock_results)
        self.assertEqual(results.is_draw(), 1)

    def test_is_draw_with_draw(self):
        mock_results = [[8, [4], 'Higher Card with Cuatro', 'Pepe'],
                        [8, [4], 'Higher Card with Cuatro', 'Juan']]
        results = Results(mock_results)
        self.assertEqual(results.is_draw(), 2)

    def test_is_draw_with_3_draw(self):
        mock_results = [[8, [4], 'Higher Card with Cuatro', 'Pepe'],
                        [8, [4], 'Higher Card with Cuatro', 'Juan'],
                        [8, [4], 'Higher Card with Cuatro', 'Rosa']]
        results = Results(mock_results)
        self.assertEqual(results.is_draw(), 3)

    def test_tiebrake_with_one_winner(self):
        mock_results = [[7, [4, 5], 'Pair with Cinco and Cuatro', 'Pepe'],
                        [7, [7, 4], 'Pair with Siete and Cuatro', 'Juan'],
                        [8, [4], 'Higher Card with Cuatro', 'Rosa']]
        results = Results(mock_results)
        self.assertEqual(results.tiebrake(2), 1)

    def test_change_number_of_As(self):
        results = Results([])
        results.tiebrake_results = [[7], [1]]
        results.change_number_of_As()
        self.assertEqual(results.tiebrake_results, [[7], [14]])

    def test_evaluate_hands_without_draw(self):
        mock_results = [[7, [4, 5], 'Pair with Cinco and Cuatro', 'Pepe'],
                        [7, [7, 4], 'Pair with Siete and Cuatro', 'Juan'],
                        [8, [4], 'Higher Card with Cuatro', 'Rosa']]
        results = Results(mock_results)
        mock_tiebrake = [[4, 5], [7, 4]]
        results.tiebrake_results = mock_tiebrake
        self.assertEqual(results.evaluate_hands(), 1)

    def test_evaluate_hands_with_draw(self):
        mock_results = [[7, [5, 4], 'Pair with Cinco and Cuatro', 'Pepe'],
                        [7, [5, 4], 'Pair with Cinco and Cuatro', 'Juan'],
                        [8, [4], 'Higher Card with Cuatro', 'Rosa']]
        results = Results(mock_results)
        mock_tiebrake = [[5, 4], [5, 4]]
        results.tiebrake_results = mock_tiebrake
        self.assertEqual(results.evaluate_hands(), 2)

    def test_is_compound_hand(self):
        results = Results([])
        self.assertEqual(results.is_compound_hand([7, 5]), True)

    def test_is_compound_hand_False(self):
        results = Results([])
        self.assertEqual(results.is_compound_hand([7]), False)

    def test_evaluate_cards_without_draw(self):
        mock_results = [[7, [6, 4], 'Pair with Seis and Cuatro', 'Pepe'],
                        [7, [5, 2], 'Pair with Cinco and Dos', 'Juan'],
                        [8, [4], 'Higher Card with Cuatro', 'Rosa']]
        results = Results(mock_results)
        mock_tiebrake = [[6, 4], [5, 2]]
        results.tiebrake_results = mock_tiebrake
        self.assertEqual(results.evaluate_cards(0, 2), 1)

    def test_evaluate_cards_with_draw(self):
        mock_results = [[7, [5, 4], 'Pair with Cinco and Cuatro', 'Pepe'],
                        [7, [5, 2], 'Pair with Cinco and Dos', 'Juan'],
                        [8, [4], 'Higher Card with Cuatro', 'Rosa']]
        results = Results(mock_results)
        mock_tiebrake = [[5, 4], [5, 2]]
        results.tiebrake_results = mock_tiebrake
        self.assertEqual(results.evaluate_cards(0, 2), 2)

    def test_change_order_of_players(self):
        mock_results = [[7, [3, 2], 'Pair with Tres and Cuatro', 'Pepe'],
                        [7, [5, 2], 'Pair with Cinco and Dos', 'Juan'],
                        [8, [4], 'Higher Card with Cuatro', 'Rosa']]
        results = Results(mock_results)
        mock_tiebrake = [[3, 2], [5, 2]]
        results.tiebrake_results = mock_tiebrake
        results.change_order_of_players(1)
        self.assertEqual(results.results[0],
                         [7, [5, 2], 'Pair with Cinco and Dos', 'Juan'])
        self.assertEqual(results.tiebrake_results, [[5, 2], [3, 2]])

    def test_players_with_draw(self):
        mock_results = [[7, [3, 2], 'Pair with Tres and Dos', 'Pepe'],
                        [7, [3, 2], 'Pair with Tres and Dos', 'Juan'],
                        [8, [4], 'Higher Card with Cuatro', 'Rosa']]
        results = Results(mock_results)
        self.assertEqual(results.players_with_draw(2),
                         'There is a draw between Pepe Juan with '
                         + 'Pair with Tres and Dos')
