'''
            --  实现线段树  --

        SegmentTree类：

            size：返回线段树长度
            get：得到索引为index的值
            _leftChild： 返回线段树中，一个索引所表示的元素的左孩子节点的索引
            _rightChild：返回线段树中，一个索引所表示的元素的右孩子节点的索引
            query：区间求和操作
            set：修改index索引的值，并重新得到线段树
            _print：方便用户查看线段树的结构

            Made by JinFan  --  2019.09.27

'''





class SegmentTree:

    def __init__(self, data):

        self._data = data
        self._tree = [None for i in range(len(data)*4)]
        self._buildSegmentTree(0, 0, len(data)-1)

    def size(self):
        return len(self._data)

    def get(self, index):

        assert index >= 0 and index < len(self._data), "Index is illegal!"
        return self._data[index]

    def _leftChild(self, k):
        return 2*k + 1

    def _rightChild(self, k):
        return 2*k + 2

    def _buildSegmentTree(self, treeIndex, l, r):

        if r == l:
            self._tree[treeIndex] = self._data[l]
            return
        leftTreeIndex = self._leftChild(treeIndex)
        rightTreeIndex = self._rightChild(treeIndex)
        mid = l + (r-l) // 2
        self._buildSegmentTree(leftTreeIndex, l, mid)
        self._buildSegmentTree(rightTreeIndex, mid+1, r)
        self._tree[treeIndex] = self._tree[leftTreeIndex] + self._tree[rightTreeIndex]

    def query(self, queryL, queryR):

        assert queryL >= 0 and queryL < len(self._data) and queryR >= 0 and \
            queryR <= len(self._data)-1 and queryL <= queryR, "Index is illegal!"

        return self._query(0, 0, len(self._data)-1, queryL, queryR)

    def _query(self, treeIndex, l, r, queryL, queryR):

        if queryL == l and queryR == r:
            return self._tree[treeIndex]

        leftChild = self._leftChild(treeIndex)
        rightChild = self._rightChild(treeIndex)
        mid = l + (r - l) // 2

        if queryL >= mid+1:
            return self._query(rightChild, mid+1, r, queryL, queryR)
        elif queryR <= mid:
            return self._query(leftChild, l, mid, queryL, queryR)

        leftResult = self._query(leftChild , l , mid , queryL , mid)
        rightResult = self._query(rightChild , mid+1 , r , mid+1 , queryR)

        return leftResult + rightResult

    def set(self, index, elem):

        assert index >= 0 and index < len(self._data), "Index is illegal!"
        self._data[index] = elem
        self._set(0, 0, len(self._data)-1, index, elem)
        return self

    def _set(self, treeIndex, l, r, index, elem):

        if l == r:
            self._tree[treeIndex] = elem
            return

        mid = l + (r - l) // 2
        leftTreeIndex = self._leftChild(treeIndex)
        rightTreeIndex = self._rightChild(treeIndex)

        if index >= mid+1:
            self._set(rightTreeIndex, mid+1, r, index, elem)
        else:
            self._set(leftTreeIndex, l, mid, index, elem)

        self._tree[treeIndex] = self._tree[leftTreeIndex] + self._tree[rightTreeIndex]

    def _print(self):

        res = '['
        for i in range(len(self._tree)):
            if self._tree[i] != None:
                res += str(self._tree[i])
            else:
                res += "null"
            if i != len(self._tree)-1:
                res += ', '
        res += "]"
        return res

    def __repr__(self):

        return "SegmentTree: %s" % self._print()


# 测试
if __name__ == "__main__":

    data = [-2, 0, 3, -5, 2, -1]
    segtree = SegmentTree(data)
    print(segtree.size())
    print(segtree.query(0,2))
    print(segtree)
    print(segtree.get(0))
    print(segtree.set(0, 100))
    print("-----------------------------------------------")
    print("success!")


