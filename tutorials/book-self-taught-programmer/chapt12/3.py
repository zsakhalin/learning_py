class Triangle:
    def __init__(self, height, baseSide):
        self.height = height
        self.baseSide = baseSide

    def findArea(self):
        return self.height * self.baseSide / 2


t1 = Triangle(1, 2)
print(t1.findArea())