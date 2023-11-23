class Person:
    def __init__(self, name):
        self.name = name


class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider


pers1 = Person("personName")
horse1 = Horse("horseName", pers1)
print(horse1.rider.name)