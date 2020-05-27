'''
    使用链表这种数据结构 构造队列，在进队和出队两个操作很难同时达到0（1）复杂度，
    这时候给链表增加一个尾节点，就变成进行0（1）复杂度了

    Node类：
        初始化一个节点

    LinkedList_Queue类：

        size：返回队列长度
        isEmpty：判断队列是否为空
        enqueue：进队操作
        dequeue：出队操作
        getFront：查看下一个出队的元素

    Made by JinFan  -- 2019.9.23
'''



class Node:

    def __init__(self, elem, next_=None):

        self.elem = elem
        self.next = next_

class LinkedList_Queue:

    def __init__(self):

        self._tail = Node(None)
        self._head = Node(None)
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, elem):

        if self._size == 0:
            self._tail = Node(elem)
            self._head = self._tail
        else:
            self._tail.next = Node(elem)
            self._tail = self._tail.next
        self._size += 1

        return self

    def dequeue(self):

        assert self._size >= 0, "Cannot dequeue from an empty queue!"
        self._head = self._head.next
        if self._head == None:
            self._tail = None
        self._size -= 1

        return self

    def getFront(self):

        assert self._size >= 0, "Queue is empty!"
        return self._head.elem

    def _print(self):

        string = 'Queue: front '
        prev = self._head
        while prev != None:
            string += str(prev.elem) + "->"
            prev = prev.next
        string += "NULL"

        return string

    def __repr__(self):

        return "LinkedList_Queue: %s" % self._print()

# 测试链表队列
if __name__ == '__main__':

    lq = LinkedList_Queue()
    for i in range(10):
        lq.enqueue(i)
        print(lq)
    for i in range(9):
        print(lq.dequeue())

    print(lq.size())
    print(lq.isEmpty())
    print(lq.getFront())

    print("----------------------------------------")
    print("success!")
    print("This is our LinkedList_Queue:\n" + str(lq))
