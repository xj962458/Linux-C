'''
                            --  最小堆  --
                                                依托数组这个数据结构

    MinHeap类：

        size：       返回堆元素个数
        isEmpty：    判断堆是否为空
        _parent：    返回完全二叉树的数组表示中，一个索引所表示的元素的父亲节点的索引
        _leftChild： 返回完全二叉树的数组表示中，一个索引所表示的元素的左孩子节点的索引
        _rightChild：返回完全二叉树的数组表示中，一个索引所表示的元素的右孩子节点的索引
        add：        往堆里丢入一个元素
        _siftUp：    上升操作
        findMin：    找到堆里最小的元素
        extractMin： 移除堆里最小的元素
        _siftDown：  下沉操作
        replace：    替换操作

        Made by JinFan  -- 2019.09.26
'''




from primary import Array

class MinHeap:

    def __init__(self, capacity=10):

        self._arr = Array.Array(capacity)

    def size(self):
        return self._arr.size()

    def isEmpty(self):
        return self._arr.isEmpty()

    def _parent(self, index):

        assert index != 0, "index-0 doesn't have parent!"
        return (index - 1) // 2

    def _leftChild(self, index):
        return index * 2 + 1

    def _rightChild(self, index):
        return index * 2 + 2

    def add(self, elem):

        self._arr.addLast(elem)
        self._siftUp(self._arr.size()-1)

    def _siftUp(self, k):

        while k > 0 and self._arr.get(self._parent(k)) > self._arr.get(k):
            self._arr.swap(k, self._parent(k))
            k = self._parent(k)

    def findMin(self):

        assert self._arr.size() > 0, "Can not findMin when heap is empty!"
        return self._arr.get(0)

    def extractMin(self):

        ret = self.findMin()
        self._arr.swap(0, self._arr.size()-1)
        self._arr.removeLast()
        self._siftDown(0)

        return ret

    def _siftDown(self, k):

        while self._leftChild(k) < self._arr.size():
            j = self._leftChild(k)
            if j+1 < self._arr.size() and self._arr.get(j) > self._arr.get(j+1):
                j += 1
            if self._arr.get(k) < self._arr.get(j):
                break
            self._arr.swap(k, j)
            k = j

    def replace(self, elem):

        res = self.findMin()
        self._arr.set(0, elem)
        self._siftDown(0)
        return res

# 测试
if __name__ == "__main__":

    minHeap = MinHeap()
    minHeap.add(2)
    minHeap.add(3)
    minHeap.add(1)
    print(minHeap.findMin())
    print(minHeap.replace(5))
    print("--------------------")
    print(minHeap.findMin())
    minHeap.extractMin()
    print(minHeap.findMin())
    print("--------------------")
    print(minHeap.size())
    print(minHeap.isEmpty())
    print("--------------------")
    print("success!")