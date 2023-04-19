l1 = [8, 19, 148, 4]
l2 = [9, 1, 33, 83]
l3 = []
temp = []

for n1 in l1:
    temp.clear()
    for n2 in l2:
        temp.append(n1*n2)
    print(temp)
    l3.append(temp[:])      # if to append temp (not temp[:]) all items in the list will be linked and equal
print(l3)