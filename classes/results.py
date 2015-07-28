class Results():
    def __init__(self, results):
        self.results = results
        self.tiebrake_results = []

    def obtain_final_result(self):
        self.results = sorted(self.results, key=lambda player: player[0])
        winner = self.is_draw()
        if winner == 1:
            return self.results[0][-1] + ' wins with ' + self.results[0][2]
        else:
            return self.players_with_draw(winner)

    def is_draw(self):
        players_in_draw = 1
        for i in range(1, len(self.results)):
            if self.results[0][0] == self.results[i][0]:
                players_in_draw += 1
        if players_in_draw > 1:
            players_in_draw = self.tiebrake(players_in_draw)
        return players_in_draw

    def tiebrake(self, number):
        self.tiebrake_results = [self.results[i][1] for i in range(number)]
        self.change_number_of_As()
        return self.evaluate_hands()

# Change the value of the As from 1 to 14 if there is a draw
    def change_number_of_As(self):
        for i in range(len(self.tiebrake_results)):
            for j in range(len(self.tiebrake_results[i])):
                if self.tiebrake_results[i][j] == 1:
                    self.tiebrake_results[i][j] = 14

    def evaluate_hands(self):
        compound_hand = self.is_compound_hand(self.tiebrake_results[0])
        players_in_draw = self.evaluate_cards(0, len(self.tiebrake_results))
        if players_in_draw > 1 and compound_hand:
            return self.evaluate_cards(1, players_in_draw)
        return players_in_draw

    def is_compound_hand(self, hand):
        return True if len(hand) == 2 else False

    def evaluate_cards(self, number_of_card, players_to_evaluate):
        players_in_draw = 1
        better_card = self.tiebrake_results[0][number_of_card]
        for i in range(1, players_to_evaluate):
            if self.tiebrake_results[i][number_of_card] == better_card:
                players_in_draw += 1
                self.change_order_of_players(i)
            if self.tiebrake_results[i][number_of_card] > better_card:
                better_card = self.results[i][number_of_card]
                self.change_order_of_players(i)
        return players_in_draw 

    def change_order_of_players(self, number_of_player):
        self.results[0], self.results[number_of_player] = \
            self.results[number_of_player], self.results[0]
        self.tiebrake_results[0], self.tiebrake_results[number_of_player] = \
            self.tiebrake_results[number_of_player], self.tiebrake_results[0]

    def players_with_draw(self, number_of_players):
        text = 'There is a draw between '
        for i in range(number_of_players):
            text += self.results[i][-1] + ' '
        text += 'with ' + self.results[0][2]
        return text
