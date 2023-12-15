def fibonacciSequence(number):
    list = [0,1]

    if number >= 2:
        for i in range(1, number-1):
            list.append(list[i] + list[i - 1])
        return list
    elif number == 0:
        return [0]
    elif number == 1:
        return [0,1]

print(fibonacciSequence(20))
