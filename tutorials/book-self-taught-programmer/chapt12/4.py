class Hexagon:
    def __init__(self, side):
        self.side = side

    def findPerim(self):
        return 6 * self.side


h1 = Hexagon(1)
print(h1.findPerim())