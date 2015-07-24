from classes.deck_of_cards import Deck_of_cards
from classes.players import Players


class Game():
    def new_game(self):
        self.deck_of_cards = Deck_of_cards()
        self.deck_of_cards.shuffle()
        self.players = Players(self.deck_of_cards)
        self.round_number = 1

    def next_round(self):
        self.round_number += 1
        new_card = self.deck_of_cards.deal_card()
        for player in self.players.players.itervalues():
            player.hand.add_card_to_hand(new_card)

if __name__ == '__main__':
    game = Game()
    game.new_game()
    game.players.add_player('Pepe')
    game.players.add_player('Juan')
    while game.round_number < 6:
        for player in game.players.players.itervalues():
            player.print_hand()
            print 
        print game.players.who_wins()
        print
        game.next_round()
