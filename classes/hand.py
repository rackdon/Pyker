class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.numbers_in_hand = []
        self.get_numbers_in_hand()
        self.order_hand()

    def print_hand(self):
        for card in self.hand:
           print card.toString()

    def determinate_hand(self):
        result = ''
        option = 1

        while option <= 8 and result == '':
            result = self.get_result(option)
            option += 1
        return result

    def get_result (self, option):
        result = ''

        if option == 1:
            if self.have_full():
                result = 'Full'

        if option == 2:
            number_of_card = self.have_straight()
            if number_of_card != 0:
                result = 'Stright from ' + self.get_face(number_of_card - 4) + ' to '
                + self.get_face(number_of_card)

        if option == 3:
            if self.have_flush():
                result = 'Flush'

        if option == 4:
            number_of_card = self.have_four()
            if number_of_card != 0:
                result = 'Four of ' + self.get_face(number_of_card)

        if option == 5:
            number_of_card = self.have_three()
            if number_of_card != 0:
                result = 'Three of ' + self.get_face(number_of_card)

        if option == 6:
            if self.have_double_pair():
                result = 'Double Pair'

        if option == 7:
            number_of_card = self.have_pair()
            if number_of_card != 0:
                result = 'Pair of ' + self.get_face(number_of_card)

        if option == 8:
            number_of_card = self.have_higher_card()
            result = 'Higher Card with ' + self.get_face(number_of_card)

        return result

    def order_hand (self):
        for i in range(0, len(self.numbers_in_hand)-2):
            for j in range(0, len(self.numbers_in_hand)-1):
                if self.numbers_in_hand[j] > self.numbers_in_hand[j + 1]:
                    self.numbers_in_hand[j + 1], self.numbers_in_hand[j] = self.numbers_in_hand[j], self.numbers_in_hand[j + 1]
                    self.hand[j + 1], self.hand[j] = self.hand[j], self.hand[j + 1]

    def get_face_number(self, face):
        if face == 'As':
            number = 14
        if face == 'Dos':
            number = 2
        if face == 'Tres':
            number = 3
        if face == 'Cuatro':
            number = 4
        if face == 'Cinco':
            number = 5
        if face == 'Seis':
            number = 6
        if face == 'Siete':
            number = 7
        if face == 'Ocho':
            number = 8
        if face == 'Nueve':
            number = 9
        if face == 'Diez':
            number = 10
        if face == 'Jota':
            number = 11
        if face == 'Reina':
            number = 12
        if face == 'Rey':
            number = 13

        return number

    def get_face(self, number):
        if number == 14:
            face = 'As'
        if number == 2:
            face = 'Dos'
        if number == 3:
            face = 'Tres'
        if number == 4:
            face = 'Cuatro'
        if number == 5:
            face = 'Cinco'
        if number == 6:
            face = 'Seis'
        if number == 7:
            face = 'Siete'
        if number == 8:
            face = 'Ocho'
        if number == 9:
            face = 'Nueve'
        if number == 10:
            face = 'Diez'
        if number == 11:
            face = 'Jota'
        if number == 12:
            face = 'Reina'
        if number == 13:
            face = 'Rey'

        return face

    def get_numbers_in_hand(self):
        for i in range(0, len(self.hand)):
            self.numbers_in_hand.append(self.get_face_number(self.hand[i].face))

    def have_full(self):
        number_of_three = self.have_three()
        return number_of_three != 0 and self.have_pair(number_of_three) != 0

    def have_straight(self):
        for hand_position in range(0, len(self.numbers_in_hand)-2):
            if self.numbers_in_hand[hand_position] + 1 != self.numbers_in_hand[hand_position+1]:
                    return 0
        return self.numbers_in_hand[len(self.numbers_in_hand)-1]

    def have_flush(self):
        for current_card in range(1, len(self.hand)):
            if self.hand[0].suit != self.hand[current_card].suit:
                return False
        return True

    def have_four(self):
        number_of_coincidences = 1
        pdb.set_trace()
        for current_card in range(0,len(self.numbers_in_hand)-3):
            if number_of_coincidences == 4:
                break
            number_of_coincidences = 1
            for sample_card in range(current_card+1, len(self.numbers_in_hand)):
                if self.numbers_in_hand[current_card] == self.numbers_in_hand[sample_card]:
                        number_of_coincidences += 1
                        number = self.numbers_in_hand[current_card]

        return number if number_of_coincidences == 4 else 0

    def have_three(self):
        number_of_coincidences = 1
        for current_card in range(0,len(self.numbers_in_hand)-2):
            if number_of_coincidences == 3:
                break
            number_of_coincidences = 1
            for sample_card in range(current_card+1, len(self.numbers_in_hand)):
                if self.numbers_in_hand[current_card] == self.numbers_in_hand[sample_card]:
                        number_of_coincidences += 1
                        number = self.numbers_in_hand[current_card]

        return number if number_of_coincidences == 3 else 0

    def have_double_pair(self):
        number = self.have_pair()
        return number != 0 and self.have_pair(number) != 0

    def have_pair (self, used_number=0):
        for current_card in range(0, len(self.numbers_in_hand)-1):
            if self.numbers_in_hand[current_card] == used_number:
                break
            for sample_card in range(current_card+1, len(self.numbers_in_hand)):
                if self.numbers_in_hand[current_card] == self.numbers_in_hand[sample_card]:
                        return self.numbers_in_hand[current_card]
        return 0

    def have_higher_card(self):
        number = 0
        for card in self.numbers_in_hand:
            if card > number:
                number = card

        return number
