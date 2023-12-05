from random import shuffle
# import Cards
from . import Cards

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Cards.Card(i, j))
        shuffle(self.cards)
        # for card in self.cards:
        #     print(card)

    def takeDeckCard(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

