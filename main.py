from classes.deck_of_cards import DeckOfCards
from classes.player import Player

my_deck_of_cards = DeckOfCards() 
my_deck_of_cards.shuffle()

player = Player(my_deck_of_cards)
player.print_hand()
print '\n', player.get_result_of_hand()
