n = str([1, 2, 3])
while 1:
    s = input("Enter int number OR x for exit\n")
    if s in n:
        print("Exist")
    else:
        print("Try again")
    if s == "x":
        break
print("you're out")