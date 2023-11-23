class Rectangle:
    rectList = []                                   # переменная класса

    def __init__(self, width, length):
        self.width = width                          # переменные экземпляра класса
        self.length = length
        self.rectList.append((self.width, self.length))
        print()

    def calculatePerim(self):
        return 2 * self.width + 2 * self.length

    def __repr__(self):
        return f"sides [{self.width}, {self.length}]"


r1 = Rectangle(1, 2)
r2 = Rectangle(10, 20)
r3 = Rectangle(100, 200)

print(Rectangle.rectList)                           # обращение к переменной класса


print(r1)                       # вызывается магический метод _repr_ и получается что-то типа
                                # <__main__.Rectangle object at 0x0000023E51AB8150>
                                # но тут _repr_ переопределён в классе Rectangle, поэтому выводится "sides[w,l]"


def isSame(a, b):
    if a is b:
        print(True)
    else:
        print(False)

isSame(r1, r1)
isSame(r1, r2)