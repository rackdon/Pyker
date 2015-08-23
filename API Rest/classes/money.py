class Money:
    def __init__(self):
        self.current_money = 1000

    def win_money(self, quantity):
        self.current_money += quantity

    def bid_money(self, quantity):
        self.current_money -= quantity
