class Queue:
    def __init__(self):
        self._queue = []

    def push(self, x):
        self._queue.append(x)

    def pop(self, x):
        try:
            return self._queue.pop(x)
        except IndexError:
            return self._queue.pop(x)

    def count(self):
        return len(self._queue)

q = Queue()
a = 0
b = 0
for i in range(15):
    a += 1
    q.push(a)
print('Всего: ', q.count())

print(q.pop(0))
for i in range(a - 1):
    print('След.: ',q.pop(0))