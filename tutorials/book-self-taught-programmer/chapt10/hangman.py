# hangman game. user enter word. program try to guess
import random

word = list(input("Enter word\n"))
letters = len(word)
board = ["_"] * letters
alphabet = list("abcdefjhigklmnopqrstuvwxyz")
while letters >= 1:
    letter = "".join(random.sample(alphabet, 1))
    try:
        board[word.index(letter)] = letter
    except ValueError:
        print("try again")
    letters -= 1
print(board)