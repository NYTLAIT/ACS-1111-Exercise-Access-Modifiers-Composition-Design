import random

class Card:
    def __init__(self, name, suit, value, color):
        self.name = name
        self.suit = suit
        self.value = value
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
            {"suit": "hearts", "color": "red"},
            {"suit": "clubs", "color": "black"},
            {"suit": "diamonds", "color": "red"},
            {"suit": "spades", "color": "black"}
            ]
        names_values = [()]

        # names = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

        # for suit_color in suits_colors:
        #     for i in range(13):
        #         card = Card(names[i], suit_color["suit"], i + 1, suit_color["color"])
        #         fresh_deck.append(card)
        # self.cards = fresh_deck

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        draw = random.randint(0, len(self.cards) - 1)
        self.cards[draw].show()

    def discard(self):
        pass
    

        
