from . import Cards, Decks, Players
class Game:
    def __init__(self):
        self.deck = Decks.Deck()
        playerName1 = input("enter player1's name: ")
        playerName2 = input("enter player2's name: ")
        self.player1 = Players.Player(playerName1)
        self.player2 = Players.Player(playerName2)

    def wins(self, winner):
        print(f"{winner} takes cards")

    def winnerDetermination(self, player1, player2):
        if player1.wins > player2.wins:
            return player1.name
        elif player1.wins < player2.wins:
            return player2.name
        else:
            return "Draw!"

    def play(self):
        print("Shuffling the deck..\nLets the game begin!")
        cardsDeck = self.deck.cards
        while len(cardsDeck) >= 2:
            response = input("x for exit, any key to continue: ")
            if response == "x" or response == "X":
                print("You choose to cancel the game. Good bye!")
                exit()
            player1TakesCard = self.deck.takeDeckCard()
            player2TakesCard = self.deck.takeDeckCard()
            print(f"{self.player1.name} puts {player1TakesCard}")
            print(f"{self.player2.name} puts {player2TakesCard}")

            if player1TakesCard > player2TakesCard:
                self.player1.wins += 1
                self.wins(self.player1.name)
            else:
                self.player2.wins += 1
                self.wins(self.player2.name)
        print("The bottom of the deck is reached. Game over!\nDetermination of the winner...")
        winner = self.winnerDetermination(self.player1, self.player2)
        print(f"{winner}")


