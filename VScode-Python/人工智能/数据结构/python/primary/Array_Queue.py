from primary import Array

class Array_Queue:

    def __init__(self):

        self._queue = Array.Array()

    def size(self):
        return self._queue.size()

    def isEmpty(self):
        return self._queue.isEmpty()

    def getFront(self):
        return self._queue.getFirst()

    def dequeue(self):
        return self._queue.removeFirst()

    def enqueue(self, elem):
        return self._queue.addLast(elem)
