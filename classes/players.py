from player import Player


class Players():
    def __init__(self, deck):
        self.deck_of_cards = deck
        self.players = {}

    def add_player(self, name):
        self.players.update({name: Player(self.deck_of_cards, name)})

    def remove_player(self, name):
        del self.players[name]

    def who_wins(self):
        pass
