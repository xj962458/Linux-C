'''
                   --  并查集  --

        UnionFind类：

            size：获取并查集长度
            isConnected：区间 p ，q 是否相通
            unionElements：连通区间 p ，q

        Made by JinFan  --  2019.09.27
'''





class UnionFind:

    def __init__(self, size):

        self._parent = [i for i in range(size)]
        self._rank = [1 for i in range(size)]

    def size(self):
        return len(self._parent)

    def _find(self, p):

        assert p >= 0 and p < len(self._parent), "p is out of bound!"
        while p != self._parent[p]:
            self._parent[p] = self._parent[self._parent[p]]
            p = self._parent[p]

        return p

    def isConnected(self, p, q):
        return self._find(p) == self._find(q)

    def unionElements(self, p, q):

        pRoot = self._find(p)
        qRoot = self._find(q)

        if pRoot == qRoot:
            return

        if self._rank[pRoot] < self._rank[qRoot]:
            self._parent[pRoot] = qRoot
        elif self._rank[pRoot] > self._rank[qRoot]:
            self._parent[qRoot] = pRoot
        else:
            self._parent[qRoot] = pRoot
            self._rank[pRoot] += 1


# 测试
if __name__ == "__main__":

    un = UnionFind(10)
    print(un.size())
    print(un.isConnected(2,7))
    un.unionElements(4,7)
    print(un.isConnected(4,7))
    print("--------------------")
    print("success!")