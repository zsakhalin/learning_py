class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculatePerim(self):
        return 2 * self.width + 2 * self.length

class Square:
    def __init__(self, width):
        self.width = width

    def calculatePerim(self):
        return self.width * 4

    def changeSize(self, addNum):
        self.width += addNum


rect1 = Rectangle(1, 2)
print(rect1.calculatePerim())
square1 = Square(1)
print(square1.calculatePerim())