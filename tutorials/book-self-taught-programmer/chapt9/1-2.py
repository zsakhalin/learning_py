# open file to read
with open("file_io.py", "r") as file:
    print(file.read())
    print(file.read())  # can't use .read 2 times

text = input("enter your text:  ")

with open("new.txt", "w+") as file:
    file.write(text)
    print(file.read())  # can't .read after .write
