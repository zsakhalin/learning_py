import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        pass

    def findArea(self):
        return math.pi * pow(self.radius, 2)


c1 = Circle(1)
print(c1.findArea())
