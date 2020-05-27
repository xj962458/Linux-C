from primary import Array

class Array_Stack:

    def __init__(self):

        self._arr = Array.Array(10)

    def size(self):
        return self._arr.size()

    def isEmpty(self):
        return self._arr.isEmpty()

    def pop(self):
        return self._arr.removeLast()

    def push(self, elem):
        return self._arr.addLast(elem)

    def peek(self):
        return self._arr.getLast()
