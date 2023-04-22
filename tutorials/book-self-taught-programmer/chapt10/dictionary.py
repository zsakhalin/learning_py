import csv
import random


def randomWord(maxLength=4):
    words = []
    with open("dictionaryEN.csv", "r") as file_obj:
        csv_obj = csv.reader(file_obj)
        for row in csv_obj:
            if len(row[0]) <= maxLength:
                words.append(row[0])

    word = "".join(random.sample(words, 1)).lower()
    # print(words)
    return word

# print(randomWord(3))