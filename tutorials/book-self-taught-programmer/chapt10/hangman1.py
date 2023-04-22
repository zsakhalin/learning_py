# hangman game. program choose the word. user try to guess
import random
import dictionary

word = dictionary.randomWord(3)
attempts = 0
letters = len(word)
dash = ["_"] * letters
alphabet = list("abcdefjhigklmnopqrstuvwxyz")
stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]

# while attempts >= 1:
for stage in stages:
    # letter = input("Enter letter: ")
    letter = "".join(random.sample(alphabet, 1))
    attempts += 1
    try:
        dash[word.index(letter)] = letter
        print(dash)
    except ValueError:
        # print("try again")
        for i in range(attempts):
            print(stages[i])

print(dash)
print(word)