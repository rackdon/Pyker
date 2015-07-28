from classes.deck_of_cards import Deck_of_cards
from classes.players import Players
from classes.game import Game


class Table():
    def __init__(self):
        self.deck_of_cards = Deck_of_cards()
        self.players = Players(self.deck_of_cards)
        self.game = None

    def new_game(self):
        self.game = Game(self.deck_of_cards, self.players)


if __name__ == '__main__':
    table = Table()
    table.players.add_player('Pepe')
    table.players.add_player('Juan')
    table.players.add_player('Rosa')
    table.new_game()
    while table.game.rounds.round_number < 4:
        for player in table.players.players.itervalues():
            print player.player_name
            player.print_hand()
            print
        print table.players.who_wins()
        table.game.rounds.next_round()
