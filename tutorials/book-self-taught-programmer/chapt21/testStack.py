from Stacks import Stack

s = Stack()

for i in range(5):
    s.push(i)
lastItem = s.peek()
a = s.pop()
b = s.push("test")
length = s.getSize()

#reversing string with stack
str = "123456789"
reversStr = ""
stack = Stack()
for i in str:
    stack.push(i)
for i in range(stack.getSize()):
    reversStr += stack.pop()
print(reversStr)