#tuple = tuple() = (,)
tup = (1,2,3)
print(tup)
print(tup[1])

try:
    tup[0] = 10 #incorrect
except TypeError:
    print("TypeError: 'tuple' object does not support item assignment")

try:
    tup = (30,) #correct
    print(tup)
except TypeError:
    print("err")