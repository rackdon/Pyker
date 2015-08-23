class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def to_string(self):
        return str(self.face) + ' of ' + str(self.suit)
