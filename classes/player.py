from hand import Hand

class Player:
    def __init__(self, deck_of_cards):
        self.hand = Hand(deck_of_cards.deal_hand())

    def get_result_of_hand(self):
        return 'The player has ' + self.hand.determinate_hand()

    def print_hand(self):
        self.hand.print_hand()
