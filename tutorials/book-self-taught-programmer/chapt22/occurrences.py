# counting occurrences of characters

def countOccurrencesOfChar(string):
    dict = {}
    for char in string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

str = "lorem ipsum dolor"
print(countOccurrencesOfChar(str))