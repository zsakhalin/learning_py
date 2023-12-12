from Queues import Queue

q = Queue()
for i in range(5, 10): #filling the queue
    q.enqueue(i)
print(q.items)
size = q.getSize()

for i in range(size): #clearing the queue
    print(q.dequeue())
    # print(f"{i} \t {q.dequeue()}")
    # print(q.items)