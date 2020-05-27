'''
            --  模拟动态数组实现映射Map  --

    ArrayMap类：

        size：       返回映射长度
        isEmpty：    判断映射是否为空
        _resize：    动态数组的实现方式
        _getIndex：  辅助函数，用来返回键Key的索引，不存在就返回-1
        add：        增加一组键值对
        contains：   看是否包含键值对key-value
        set：        重新设置value值，不存在键key即返回报错信息
        get：        得到key对应的值
        remove：     删除一组键值对
        _print：     方便用户输出

        Made by JinFan  --  2019.09.25
'''




class ArrayMap:

    def __init__(self, capacity=10):

        self._capacity = capacity
        self._key = []
        self._value = []
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def _resize(self, capacity):

        self._capacity = capacity

    def _getIndex(self, k):

        for i in range(self._size):
            if self._key[i] == k:
                return i
        return -1

    def add(self, k, v):

        if self._size == self._capacity:
            self._resize(2*self._capacity)
        n = self._getIndex(k)
        if n != -1:
            self._value[k] = v
        else:
            self._key.append(k)
            self._value.append(v)
            self._size += 1

        return self

    def contains(self, k):
        return self._getIndex(k) != -1

    def set(self, k, v):

        n = self._getIndex(k)
        assert n != -1, k + "doesn't exist!"
        self._value[n] = v

        return self

    def get(self, k):

        n = self._getIndex(k)
        if n == -1:
            return None
        return self._value[n]

    def remove(self, k):

        n = self._getIndex(k)
        if n == -1:
            return
        else:
            v = self._value[n]
            for i in range(n, self._size-1):
                self._key[i] = self._key[i+1]
                self._value[i] = self._value[i+1]
            self._size -= 1
            if self._size == self._capacity / 4 and self._capacity != 1:
                self._resize(self._capacity / 2)

            return v

    def _print(self):

        string = '{'
        for i in range(self._size):
            string += str(self._key[i]) + ":" + str(self._value[i])
            if i != self._size-1:
                string += ','
        string += '}'

        return string

    def __repr__(self):

        return "ArrayMap: %s" % self._print()


# 测试
if __name__ == "__main__":

    arrmap = ArrayMap()
    arrmap.add('jinfan',123456)
    arrmap.add("haha",'吃饭')
    print(arrmap)
    print('------------------------------')
    print(arrmap.remove(4))
    print(arrmap.remove("jinfan"))
    print(arrmap)
    print('------------------------------')
    print(arrmap.size())
    print(arrmap.isEmpty())
    print(arrmap.get('haha'))
    print(arrmap.contains('haha'))
    print(arrmap.set("haha", "不吃饭"))
    print('------------------------------')
    print("success!")

