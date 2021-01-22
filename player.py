class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def remove_card(self):
        return self.all_cards.pop(0)

    def __str__(self):
        return "Player "+self.name + " has "+ len(self.all_cards) + " cards"

