import random

class Card:
    def __init__(self, name, suit, num_value, color):
        self.name = name
        self.suit = suit
        self.num_value = num_value
        self.color = color

    def show(self):
        print(f'Name: {self.name} Suit: {self.suit}')

class Deck:
    def __init__(self, cards=[]):
        self.cards = cards
        self.discard_pile = []

    def fresh_deck(self):
        fresh_deck = []
        suits_colors = [
            ("hearts", "red"),
            ("clubs", "black"),
            ("diamonds", "red"),
            ("spades", "black")
            ]
        names_values = [
            ("Ace", 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), 
            (8, 8), (9, 9), (10, 10), ("Jack", 11), ("Queen", 12), ("King", 13)
            ]
        for suit, color in suits_colors:
            for name, value in names_values:
                card = Card(name, suit, value, color)
                fresh_deck.append(card)
        self.cards = fresh_deck

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        draw = random.randint(0, len(self.cards) - 1)
        self.cards[draw].show()

    def discard(self):
        pass
    

        
