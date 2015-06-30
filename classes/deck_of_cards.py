 # coding=utf-8
import random

from card import Card

class DeckOfCards:
    def __init__(self):
        self.__number_of_cards = 52
        self.current_card = 0
        self.deck = []
        self.faces = ['As', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete',
                'Ocho', 'Nueve', 'Diez', 'Jota', 'Reina', 'Rey']
        self.suits = ['Corazones', 'Diamantes', 'Tréboles', 'Espadas']

        for i in range(self.__number_of_cards):
            self.deck.append( Card(self.faces[i%13], self.suits[i/13]) )

    def shuffle(self):
       for position in range(len(self.deck)):
          second = random.randrange(self.__number_of_cards)
          temp = self.deck[position]
          self.deck[position] = self.deck[second]
          self.deck[second] = temp
    
    def deal_hand(self):
        hand = []
        for i in range(5):
            hand.append(self.deck[self.current_card])
            self.current_card += 1
        return hand
