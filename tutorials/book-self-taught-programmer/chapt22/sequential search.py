# sequential search - последовательный поиск

def isFound(list, item):
    count = 0
    while count < len(list):
        if item == list[count]:
            return True
        count += 1
    return False

list = [i for i in range(1, 11)]
item = 0
print(len(list))
print(isFound(list, item))