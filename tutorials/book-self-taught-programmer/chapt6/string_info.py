str = "1234"    # string
print(str[0])   # 1
print(str[1])   # 2
print(str[-1])  # 4
print(str*2)    # 12341234

str1 = "abcd"
print(str1.upper())    # ABCD
print(str1.capitalize())    # Abcd

variable = "variable of any type"
formatted_str = "some text includes variable content between curl brackets - {} ".format(variable)
print(formatted_str)

# string.split("symbol")
sentences = "hello. what a glory hammer?"
sentences_list = sentences.split(".")   # returns list
print(sentences_list)

# string.join(other string)
str = "abcd"
print("/".join(str) + ".")
list1 = ["1", "2", "3", "4"]
print(list1)
print("".join(list1))
print("wedfgh".join("@1"))

# " string with spaces at the beginning and end    ".strip() remove start and end spaces

# replace
srt2 = "dfghatjgf.gn \n hello, user"    #\n - new line
print(srt2.replace("at", "@"))

# str.index("symbol") = returns symbol's index

# membership tests, (i.e. the in and not in expressions)
str3 = "some text"
print("some" in str3)   # True
print("Some1" in str3)   # False
print("Some1" not in str3)   # True

# slicing on string (list, tuple)
str4 = "0123456"
print(str4[0:4])    # 0123
print(str4[:4])     # 0123
print(str4[3:])     # 3456