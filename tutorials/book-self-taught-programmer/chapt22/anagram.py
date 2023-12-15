def isAnagram(sequence1, sequence2):
    return sorted(sequence1) == sorted(sequence2)

str1 = "listen"
str2 = "silent"
list = [1,2,3]
dict = {1:1,2:2,5:4}
tuple = ()

print(isAnagram("",""))
print(isAnagram([],[]))
print(isAnagram({},{}))
print(isAnagram((),(1,)))
print(isAnagram(list,dict))
print(isAnagram(str1,str2))