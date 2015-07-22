# coding=utf-8
import random
from card import Card


class Deck_of_cards:
    def __init__(self):
        self.__number_of_cards = 52
        self.current_card = 0
        self.faces = ('As', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete',
                      'Ocho', 'Nueve', 'Diez', 'Jota', 'Reina', 'Rey')
        self.suits = ('Corazones', 'Diamantes', 'Tréboles', 'Picas')
        self.deck = [Card(self.faces[i % 13], self.suits[i/13]) for i in
                     range(self.__number_of_cards)]

    def shuffle(self):
        for position in range(len(self.deck)):
            second = random.randrange(self.__number_of_cards)
            self.deck[position], self.deck[second] = \
                self.deck[second], self.deck[position]

    def deal_hand(self):
        hand = [self.deal_card() for i in range(5)]
        return hand

    def deal_card(self):
        self.current_card += 1
        return self.deck[self.current_card - 1]
