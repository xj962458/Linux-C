from primary import LinkedList

class LinkendList_Stack:

    def __init__(self):

        self._list = LinkedList.LinkedList()

    def size(self):
        return self._list.size()

    def isEmpty(self):
        return self._list.isEmpty()

    def pop(self):
        return self._list.removeLast()

    def push(self, elem):
        return self._list.addLast(elem)

    def peek(self):
        return self._list.getLast()
