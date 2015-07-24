from player import Player


class Players():
    def __init__(self, deck):
        self.deck_of_cards = deck
        self.players = {}
        self.results = []

    def add_player(self, name):
        self.players.update({name: Player(self.deck_of_cards, name)})

    def remove_player(self, name):
        del self.players[name]

    def who_wins(self):
        self.results = [player.get_result_of_hand() for player in
                        self.players.itervalues()]
        self.results = sorted(self.results, key=lambda player: player[0])
        winner = self.is_draw()
        if winner == 0:
            return self.results[0][-1] + ' wins with ' + self.results[0][2]
        else:
            return 'There is a draw'

    def is_draw(self):
        draws = 0
        for i in range(1, len(self.results)):
            if self.results[0][0] == self.results[i][0]:
                draws += 1
        if draws > 0:
            draws = self.tiebrake(draws)
        return draws

    def tiebrake(self, number):
        tiebrake_results = [self.results[i][1] for i in range(number+1)]
        self.change_number_of_As(tiebrake_results)
        return self.evaluate_hands(tiebrake_results)

# Change the value of the As from 1 to 14 if there is a draw
    def change_number_of_As(self, tiebrake_results):
        for i in range(len(tiebrake_results)):
            for j in range(len(tiebrake_results[i])):
                if tiebrake_results[i][j] == 1:
                    tiebrake_results[i][j] = 14

    def evaluate_hands(self, tiebrake_results):
        compound_hand = self.is_compound_hand(tiebrake_results[0])
        return self.evaluate_cards(tiebrake_results, compound_hand)

    def is_compound_hand(self, hand):
        return True if len(hand) == 2 else False

    def evaluate_cards(self, tiebrake_results, compound_hand):
        draws = self.evaluate_first_card(tiebrake_results)
        if draws > 0 and compound_hand:
            return self.evaluate_second_card(tiebrake_results, draws)
        return draws

    def evaluate_first_card(self, tiebrake_results):
        draws = 0
        better_card = tiebrake_results[0][0]
        for i in range(1, len(tiebrake_results)):
            if tiebrake_results[i][0] == better_card:
                draws += 1
                self.change_order_of_players(i, tiebrake_results)
            if tiebrake_results[i][0] > better_card:
                better_card = self.results[i][0]
                self.change_order_of_players(i, tiebrake_results)
        return draws if draws > 0 else 0

    def evaluate_second_card(self, tiebrake_results, draws):
        second_draws = 0
        better_card = tiebrake_results[0][1]
        for i in range(1, draws + 1):
            if tiebrake_results[i][1] == better_card:
                second_draws += 1
                self.change_order_of_players(i, tiebrake_results)
            if tiebrake_results[i][1] > better_card:
                better_card = self.results[i][1]
                self.change_order_of_players(i, tiebrake_results)
        return second_draws if second_draws > 0 else 0

    def change_order_of_players(self, number_of_player, tiebrake_results):
        self.results[0], self.results[number_of_player] = \
            self.results[number_of_player], self.results[0]
        tiebrake_results[0], tiebrake_results[number_of_player] = \
            tiebrake_results[number_of_player], tiebrake_results[0]
