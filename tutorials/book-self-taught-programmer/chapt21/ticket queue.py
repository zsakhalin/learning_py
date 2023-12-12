# modeling of queue for tickets
import Queues
from datetime import datetime, timedelta, tzinfo, timezone
import random, time

d = datetime(1944, 12, 29, 21)
d1 = datetime(1944, 12, 31, 20)
print(d - d1)
print(d)
print(timedelta(hours=4))
d2 = d1 + timedelta(minutes=random.randint(1, 5))
print(d)
print(d2)
print(d2 - d)


def line(queue, finalTime, maxSellTime):
    buyers = []
    currentTime = datetime.now()
    while currentTime < finalTime and not queue.isEmpty():
        buyers.append(queue.dequeue())
        randSellTime = timedelta(minutes=random.randint(1, maxSellTime))
        currentTime += randSellTime
    return len(buyers)


viewers = Queues.Queue()
amountOfViewers = 100
showTime = datetime(2023, 12, 13, 10)
maxSellTime = 10  # minutes
for i in range(1, amountOfViewers + 1):
    viewers.enqueue("person " + str(i))

print(line(viewers, showTime, maxSellTime))
