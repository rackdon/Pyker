from hand import Hand


class Player:
    def __init__(self, deck_of_cards, name):
        self.hand = Hand(deck_of_cards.deal_hand())
        self.player_name = name

    def get_result_of_hand(self):
        return '%s has %s' % \
               (self.player_name, self.hand.determinate_hand())

    def print_hand(self):
        self.hand.print_hand()
