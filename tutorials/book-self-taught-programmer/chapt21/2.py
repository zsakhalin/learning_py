import Stacks

list = [i for i in range(11)]
reversList = []
s = Stacks.Stack()

for i in list:
    s.push(i)

print(s.items)

for j in range(s.getSize()):
    reversList.append(s.pop())

print(reversList)