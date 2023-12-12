#revers the string
import Stacks

str = "позавчера"
reversStr = ""
s = Stacks.Stack()

for i in str:
    s.push(i)
for j in range(s.getSize()):
    reversStr += s.pop()

print(reversStr)