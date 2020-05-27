'''
    这是一颗二分搜索树

    Node类：
        初始化节点

    BSTree类：

        size：       返回树中元素个数
        isEmpty：    判断是否为一颗空树
        add：        给树增加一个元素
        contains：   判断树中是否有元素elem
        preOrder：   从小到大输出树中元素
        findMin：    找到树中最小元素
        findMax：    找到树中最大元素
        removeMin：  删除树中最小的元素
        removeMax：  删除树中最大元素
        remove：     删除指定元素elem，若树中没有elem，则不删除任何元素

        Made by JinFan -- 2019.09.24
'''



class Node:

    def __init__(self, elem=None, left_=None, right_=None):

        self.elem = elem
        self.left = left_
        self.right = right_

class BSTree:

    def __init__(self):

        self._root = Node(None, Node(), Node())
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add(self, elem):
        self._root = self._add(self._root, elem)

    def _add(self, node, elem):

        if node.elem == None:
            self._size += 1
            return Node(elem, Node(), Node())
        if elem < node.elem:
            node.left = self._add(node.left, elem)
        elif elem > node.elem:
            node.right = self._add(node.right, elem)

        return node

    def contains(self, elem):
        return self._contains(self._root, elem)

    def _contains(self, node, elem):

        if node.elem == None:
            return False
        if elem < node.elem:
            return self._contains(node.left, elem)
        elif elem == node.elem:
            return True
        else:
            return self._contains(node.right, elem)

    def preOrder(self):
        self._preOrder(self._root)

    def _preOrder(self, node):

        if node.elem == None:
            return
        print(node.elem)
        self._preOrder(node.left)
        self._preOrder(node.right)

    def findMin(self):
        return self._findMin(self._root).elem

    def _findMin(self, node):

        if node.left.elem == None:
            return node

        return self._findMin(node.left)

    def findMax(self):
        return self._findMax(self._root).elem

    def _findMax(self, node):

        if node.right.elem == None:
            return node

        return self._findMax(node.right)

    def removeMin(self):

        assert self._size >= 0, "Can not delete from 0 size!"
        node = self._findMin(self._root)
        self._root = self._removeMin(self._root)

        return node.elem

    def _removeMin(self, node):

        if node.left.elem == None:
            rightNode = node.right
            node.right = None
            self._size -= 1
            return rightNode
        node.left = self._removeMin(node.left)

        return node

    def removeMax(self):

        assert self._size >= 0, "Can not delete from 0 size!"
        node = self._findMax(self._root)
        self._root = self._removeMax(self._root)

        return node.elem

    def _removeMax(self, node):

        if node.right.elem == None:
            leftNode = node.left
            node.left = None
            self._size -= 1
            return leftNode
        node.right = self._removeMax(node.right)

        return node

    def remove(self, elem):

        assert self._size >= 0, "Can not delete from 0 size!"
        self._root = self._remove(self._root, elem)

    def _remove(self, node, elem):

        if node.elem == None:
            return Node()
        if elem < node.elem:
            node.left = self._remove(node.left, elem)
            return node
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
            return node
        else:
            if node.left.elem == None:
                rightNode = node.right
                node.right = None
                self._size -= 1
                return rightNode
            if node.right.elem == None:
                leftNode = node.left
                node.left = None
                self._size -= 1
                return leftNode

            successor = self._findMin(node.right)
            successor.right = self._removeMin(node.right)
            successor.left = node.left
            node.left = node.right = None

            return successor

# 测试二分树
if __name__ == '__main__':
    bst = BSTree()
    bst.add(2)
    bst.add(3)
    bst.add(1)
    bst.add(4)
    bst.add(5)
    print(bst.findMin())
    print(bst.findMin())
    print(bst.findMin())
    print(bst.isEmpty())
    print(bst.size())
    bst.preOrder()
    print("------")
    print("------")
    print(bst.removeMax())
    print(bst.findMax())
    print("------")
    bst.remove(9)
    bst.remove(3)
    print(bst.size())
    print("----------------------------")
    print("success!")