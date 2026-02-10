import random

class Card:
    def __init__(self, suit, value, color):
        self.suit = suit
        self.value = value
        self.color = color

    def show(self):
        print(f'Value: {self.value} Suit: {self.suit}')

class Deck:
    def __init__(self, cards=[]):
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
