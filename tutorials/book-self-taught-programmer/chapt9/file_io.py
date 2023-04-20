# first way to deal with file
file_obj = open("file_io.py", "r")
print(file_obj.read())
file_obj.close()    # need to close file!

# or second. File will be closed automatically.  Don't need use .close

with open("file_io.py", "r") as file_obj:
    print(file_obj.read())