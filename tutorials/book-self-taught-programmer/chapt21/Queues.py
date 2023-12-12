# FIFO = first-in-first-out
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def getSize(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
