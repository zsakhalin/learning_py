class Card:
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["spades", "hearts", "diamonds", "clubs"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        # print("done")

    def __lt__(self, other):            # self <= other
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
        else:
            return False
        return False

    def __gt__(self, other):            # self  => other
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        r = self.values[self.value] + " " + self.suits[self.suit]
        return r