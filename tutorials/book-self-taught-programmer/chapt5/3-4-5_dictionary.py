# dictionary = dict() = {}
author_song = {"singer1":"song name1",
               "singer2":"song name2"}
info = {"name": "tony",
        "age": 60,
        }

question = input("what want you to know? ")

if question in info:
    print(info[question])
else:
    print("I don't know -\\0/-")