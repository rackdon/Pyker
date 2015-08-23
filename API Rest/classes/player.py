from hand import Hand
from money import Money


class Player:
    def __init__(self, deck_of_cards, name):
        self.deck = deck_of_cards
        self.player_name = name
        self.new_hand()
        self.money = Money()

    def get_result_of_hand(self):
        result = self.hand.determinate_hand()
        result.append(self.player_name)
        return result

    def new_hand(self):
        self.hand = Hand(self.deck.deal_hand())

    def print_hand(self):
        self.hand.print_hand()
