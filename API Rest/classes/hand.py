from operator import itemgetter
from itertools import groupby

face_number = {'As': 1,
               'Dos': 2,
               'Tres': 3,
               'Cuatro': 4,
               'Cinco': 5,
               'Seis': 6,
               'Siete': 7,
               'Ocho': 8,
               'Nueve': 9,
               'Diez': 10,
               'Jota': 11,
               'Reina': 12,
               'Rey': 13}

face_of_the_number = ['', 'As', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis',
                      'Siete', 'Ocho', 'Nueve', 'Diez', 'Jota', 'Reina', 'Rey',
                      'As']


class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.numbers_in_hand = []
        self.get_numbers_in_hand()
        self.order_hand()

    def print_hand(self):
        for card in self.hand:
            print(card.to_string())

    def add_card_to_hand(self, card):
        self.hand.append(card)
        self.numbers_in_hand.append(self.get_face_number(card.face))
        self.order_hand()

    def determinate_hand(self):
        result = []
        option = 1
        while option <= 8 and len(result) <= 1:
            result = self.get_result(option)
            option += 1
        return result

    def get_result(self, option):
        result = [option]

        if option == 1:
            full = self.have_full()
            if isinstance(full, list):
                result.append(full)
                result.append('Full with Three of ' + self.get_face(full[0])
                              + ' and Pair of ' + self.get_face(full[1]))

        if option == 2:
            number_of_card = self.have_straight()
            if number_of_card != 0:
                result.append([number_of_card])
                result.append('Straight from '
                              + self.get_face(number_of_card - 4)
                              + ' to ' + self.get_face(number_of_card))

        if option == 3:
            flush = self.have_flush()
            if flush:
                result.append([])
                result.append('Flush of ' + flush)

        if option == 4:
            number_of_card = self.have_group(4)
            if number_of_card != 0:
                result.append([number_of_card])
                result.append('Four of ' + self.get_face(number_of_card))

        if option == 5:
            number_of_card = self.have_group(3)
            if number_of_card != 0:
                result.append([number_of_card])
                result.append('Three of ' + self.get_face(number_of_card))

        if option == 6:
            pairs = self.have_double_pair()
            if isinstance(pairs, list):
                result.append(pairs)
                result.append('Double Pair with ' + self.get_face(pairs[0])
                              + ' and '
                              + self.get_face(pairs[1]))

        if option == 7:
            number_of_card = self.have_group(2)
            if number_of_card != 0:
                result.append([number_of_card])
                result.append('Pair of ' + self.get_face(number_of_card))

        if option == 8:
            number_of_card = self.have_higher_card()
            result.append([number_of_card])
            result.append('Higher Card with ' + self.get_face(number_of_card))

        return result

    def order_hand(self):
        self.numbers_in_hand.sort()
        self.hand = sorted(self.hand,
                           key=lambda card: self.get_face_number(card.face))

    def get_face_number(self, face):
        return face_number.get(face)

    def get_face(self, number):
        return face_of_the_number[number]

    def get_numbers_in_hand(self):
        for i in range(0, len(self.hand)):
            self.numbers_in_hand.append(
                self.get_face_number(self.hand[i].face))

    def have_full(self):
        number_of_three = self.have_group(3)
        number_of_pair = self.have_group(2, number_of_three)
        return [number_of_three, number_of_pair] if number_of_three != 0 and \
            number_of_pair != 0 else 0

    def have_straight(self):
        for key, group in groupby(enumerate(
                                  self.get_non_repeated_numbers_list()),
                                  lambda (index, item): index - item):
            group = map(itemgetter(1), group)
            if len(group) > 5:
                return group[-1]
        return 0

    def get_non_repeated_numbers_list(self):
        non_repeated_numbers = list(set(self.numbers_in_hand))
        if non_repeated_numbers[0] == 1 and non_repeated_numbers[-1] == 13:
            non_repeated_numbers.append(14)
        return non_repeated_numbers

    def have_flush(self):
        suit_hand = [current_card.suit for current_card in self.hand]
        for current_suit in suit_hand:
            if suit_hand.count(current_suit) >= 5:
                return current_suit
        return False

    def have_double_pair(self):
        pair1 = self.have_group(2)
        pair2 = self.have_group(2, pair1)
        return [pair1, pair2] if pair1 != 0 and pair2 != 0 else 0

    def have_group(self, kind_of_group, used_number=0):
        group = 0
        for number in self.numbers_in_hand:
            if self.numbers_in_hand.count(number) == kind_of_group \
               and number != used_number \
               and group != 1:
                    group = number
        return group

    def have_higher_card(self):
        number = 0
        for card in self.numbers_in_hand:
            if (card > number or card == 1) and number != 1:
                number = card
        return number
