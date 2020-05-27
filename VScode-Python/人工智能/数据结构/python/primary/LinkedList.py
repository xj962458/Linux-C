'''
    Node类：
        初始化一个节点

    LinkedList类：

        size：      返回链表长度
        isEmpty：   返回链表是否为空
        add：       增加一个元素，index为插入位置
        addFirst：  在头节点处增加
        addLast：   在尾节点处增加
        remove：    删除一个元素，index为删除位置
        removeFirst：删除第一个元素
        removeLast：删除最后一个元素
        set：       修改元素，index为修改位置
        get：       获取index位置元素
        getFirst：  获取第一个元素
        getLast：   获取最后一个元素
        find：      元素第一个elem在链表中的第一个位置，没有返回-1
        removeElements：删除链表中所有elem元素
        _print:     定义私有函数，方便用户输出

        Made by JinFan  -- 2019.9.23
'''


class Node:

    def __init__(self, elem, next_=None):

        self.elem = elem
        self.next = next_

class LinkedList:

    def __init__(self):

        self._node = Node(None)
        self._iter = 0

    def size(self):
        return self._iter

    def isEmpty(self):
        return self._iter == 0

    def add(self, index, elem):

        assert index <= self._iter and index >= 0, "Index is illegal!"
        prev = self._node
        while index > 0:
            prev = prev.next
            index -= 1
        prev.next = Node(elem, prev.next)
        self._iter += 1

        return self

    def addFirst(self, elem):
        return self.add(0, elem)

    def addLast(self, elem):
        return self.add(self._iter, elem)

    def remove(self, index):

        assert index < self._iter and index >= 0, "Index is illegal!"
        dummyHead = Node(None, self._node)

        while index >= 0:
            dummyHead = dummyHead.next
            index -= 1
        dummyHead.next = dummyHead.next.next
        self._iter -= 1

        return self

    def removeFirst(self):
        return self.remove(0)

    def removeLast(self):
        return self.remove(self._iter-1)

    def set(self, index, elem):

        assert index < self._iter and index >= 0, "Index is illegal!"
        prev = self._node

        while index >= 0:
            prev = prev.next
            index -= 1
        prev.elem = elem

        return self

    def get(self, index):

        assert index < self._iter and index >= 0, "Index is illegal!"
        prev = self._node

        while index >= 0:
            prev = prev.next
            index -= 1

        return prev.elem

    def getFirst(self):
        return self.get(0)

    def getLast(self):
        return self.get(self._iter-1)

    def find(self, elem):

        index = -1
        prev = self._node
        while prev != None:
            if prev.elem == elem:
                return index
            index += 1
            prev = prev.next

        return -1

    def removeElements(self, elem):

        dummyHead = Node(None, self._node)

        while dummyHead.next != None:
            while dummyHead.next.elem == elem:
                dummyHead.next = dummyHead.next.next
                if dummyHead.next == None:
                    return self
            dummyHead = dummyHead.next

        return self


    def _print(self):

        prev = self._node.next
        string = ''
        while prev != None:
            string += str(prev.elem) + "->"
            prev = prev.next
        string += "NULL"

        return string

    def __repr__(self):

        return "LinkedList: %s" % self._print()

# 测试链表
if __name__ == "__main__":

    link = LinkedList()
    for i in range(10):
        link.addFirst(i)
        link.add(0,i)
        link.addLast(i)
    for i in range(10):
        link.remove(i)
    for i in range(10):
        link.removeLast()
        link.removeFirst()

    link.addFirst(1)
    link.addLast(1)
    link.addLast(1)
    print(link.find(1))
    print(link.find(0))
    print(link.set(0, 2))
    print(link.get(0))

    print(link.removeElements(1))

    print("----------------------------------------")
    print("success!")
    print("This is our LinkedList:\n" + str(link))

