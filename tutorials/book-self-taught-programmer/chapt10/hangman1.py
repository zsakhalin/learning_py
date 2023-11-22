# hangman game. program choose the word. user try to guess
import random
import dictionary

word = dictionary.randomWord(3)
attempts = 0
looses = 0
letters = len(word)
board = ["_"] * letters
alphabet = list("abcdefjhigklmnopqrstuvwxyz")
stages = ["________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]

# while attempts >= 1:
for stage in stages:
    letter = input("Enter letter: ")
    # letter = "".join(random.sample(alphabet, 1))
    try:
        board[word.index(letter)] = letter
        if "_" not in board:
            print("Winner winner chicken dinner!")
            break
        print(f"continue with {board}")
        continue
    except ValueError:
        print("\n".join(stages[:(attempts + 1)]) + "\n")
        looses += 1
    attempts += 1
    if looses == len(stages):
        print("Looser!")
        break

print(f"your guess: {board}")
print(word)

# TODO:
#  fix
#  if looses == len(stages):
#  when some letter guessed
