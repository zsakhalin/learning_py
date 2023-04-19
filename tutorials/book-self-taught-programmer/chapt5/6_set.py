# set = set()
set1 = set("qwerty")
print(set1)
try:
    print(set1[0]) #incorrect, set is not subscriptable
except TypeError:
    print("TypeError: 'set' object is not subscriptable")
    print(type(set1))