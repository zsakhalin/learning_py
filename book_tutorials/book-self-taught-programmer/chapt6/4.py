from random import random

questions_list = "Where is it? Who is? When?".split("?")
questions_list.pop()        # remove last item
for item in questions_list:
    item += "?"             # didn't change item
    print(item)

for i in range(len(questions_list)):
    questions_list[i] += "?"            # change item

for k, item in enumerate(questions_list):
    questions_list[k] += "["            # another way to iterate items

print(questions_list)
# print(help(list))