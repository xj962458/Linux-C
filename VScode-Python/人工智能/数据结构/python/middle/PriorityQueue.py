'''
            --  使用最大堆来实现一个优先队列  --

    PriorityQueue类：

        size：获取优先队列长度
        isEmpty：判断是否为空
        getFront：查看下一个出队的元素
        dequeue：出队操作
        enqueue：进队操作

        Made by JinFan  --  2019.09.26
'''





from middle import MaxHeap

class PriorityQueue:

    def __init__(self):

        self._maxHeap = MaxHeap.MaxHeap()

    def size(self):
        return self._maxHeap.size()

    def isEmpty(self):
        return self._maxHeap.isEmpty()

    def getFront(self):
        return self._maxHeap.findMax()

    def dequeue(self):
        return self._maxHeap.extractMax()

    def enqueue(self, elem):
        self._maxHeap.add(elem)