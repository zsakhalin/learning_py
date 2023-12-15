# Recursion
def fibonacciSequence(number):
    if number in [0,1]:
        return number
    return fibonacciSequence(number - 1) + fibonacciSequence(number - 2)

print(fibonacciSequence(15))