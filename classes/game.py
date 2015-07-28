from rounds import Rounds


class Game():
    def __init__(self, deck_of_cards, players):
        self.deck_of_cards = deck_of_cards
        self.players = players
        self.rounds = None
        self.new_game()

    def new_game(self):
        self.deck_of_cards.shuffle()
        self.deal_hands()
        self.rounds = Rounds(self)

    def deal_hands(self):
        for player in self.players.players.itervalues():
            player.new_hand()

    def deal_three_cards_on_table(self):
        for i in range(3):
            self.deal_card_on_table()

    def deal_card_on_table(self):
        new_card = self.deck_of_cards.deal_card()
        for player in self.players.players.itervalues():
            player.hand.add_card_to_hand(new_card)
