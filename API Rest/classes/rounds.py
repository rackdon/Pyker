class Rounds:
    def __init__(self, game):
        self.game = game
        self.round_number = 0

    def next_round(self):
        self.round_number += 1
        self.game.deal_three_cards_on_table() if self.round_number == 1 \
            else self.game.deal_card_on_table()
