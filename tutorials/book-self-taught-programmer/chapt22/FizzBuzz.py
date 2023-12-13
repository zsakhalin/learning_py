# print numbers 1 to 100.
# if the number is a multiple of 3, print Fizz
# if the number is a multiple of 5, print Buzz
# if the number is a multiple of 3 and 5, print FizzzBuzz

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
