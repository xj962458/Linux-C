'''
      --  模型Array的实现过程 ， 在python语言中，实现这样一个数组意义可能没那么大  --

    Array类：

        size：      返回链表长度
        isEmpty：   返回链表是否为空
        _resize：   实现动态数组
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
        swap:       用来交换数组中两个元素的位置

        Made by JinFan  -- 2019.9.24
'''



class Array:

    def __init__(self, capacity=10):

        self._capacity = capacity
        self._size = 0
        self._data = []

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def _resize(self, capacity):
        self._capacity = capacity

    def add(self, index, elem):

        assert index <= self._size and index >= 0, "Index is illegal!"
        if self._size == self._capacity:
            self._resize(2*self._capacity)
        self._data.insert(index, elem)
        self._size += 1

        return self

    def addFirst(self, elem):
        return self.add(0, elem)

    def addLast(self, elem):
        return self.add(self._size, elem)

    def remove(self, index):

        assert index < self._size and index >= 0, "Index is illegal!"
        assert self._size > 0, "Can not delete from 0 size!"
        self._data.pop(index)
        self._size -= 1

        if self._size == self._capacity / 4 and self._capacity != 1:
            self._resize(self._capacity / 2)

        return self

    def removeFirst(self):
        return self.remove(0)

    def removeLast(self):
        return self.remove(self._size-1)

    def set(self, index, elem):

        assert index < self._size and index >= 0, "Index is illegal!"
        self._data[index] = elem

        return self

    def get(self, index):

        assert index < self._size and index >= 0, "Index is illegal!"

        return self._data[index]

    def getFirst(self):
        return self.get(0)

    def getLast(self):
        return self.get(self._size-1)

    def find(self, elem):

        iter = 0
        for e in self._data:
            if e == elem:
                return iter
            iter += 1
        return -1

    def removeElements(self, elem):

        iter = self._data.count(elem)
        if iter != 0:
            for i in range(iter):
                self._data.remove(elem)

        return self

    def swap(self, i, j):

        assert i >= 0 and i < self._size and j >= 0 and j < self._size, \
                "Index is illegal!"
        temp = self._data[i]
        self._data[i] = self._data[j]
        self._data[j] = temp


    def __repr__(self):

        return str(self._data)


# 测试数组
if __name__ == "__main__":

    arr = Array(10)
    for i in range(10):
        arr.addFirst(i)
        arr.add(0,i)
        arr.addLast(i)
    for i in range(10):
        arr.remove(i)
    for i in range(10):
        arr.removeLast()
        arr.removeFirst()

    arr.addFirst(1)
    arr.addLast(1)
    arr.addLast(1)
    print(arr.find(1))
    print(arr.find(0))
    print(arr.set(0, 2))
    print(arr.get(0))

    print(arr.removeElements(1))

    print("----------------------------------------")
    print("success!")
    print("This is our Array:\n" + str(arr))
