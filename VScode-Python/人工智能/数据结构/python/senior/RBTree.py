'''
                 --  用红黑树实现映射Map  --

        此版本的缺陷是，key键只能为数字，value可以为任何数据类型的

        Node类：
            初始化一个节点

        RBMap类：

            size：       返回映射长度
            isEmpty：    判断映射是否为空
            isRed：      判断是否为红树
            _rightRotate：右旋转
            _leftRotate：左旋转
            _flipColors：颜色翻转
            _getNode：   辅助函数，用来得到树中key键对应的的节点Node，若key不存在，则返回None
            add：        增加一组键值对
            contains：   看是否包含键值对key-value
            set：        重新设置value值，不存在键key即返回报错信息
            get：        得到key对应的值
            preOrder：   输出映射中所有的键值对

        Made by JinFan  -- 2019.09.27
'''






class Node:

    def __init__(self, key=None, value=None, left_=None, right_=None, color=True):

        self.key = key
        self.value = value
        self.left = left_
        self.right = right_
        self.color = color

class RBMap:

    def __init__(self):

        self._root = Node(None, None, Node(), Node())
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0


    def isRed(self, node):
        if node == None:
            return False
        return node.color

    #    node                     x
    #   /   \     左旋转         /  \
    #  T1   x   --------->   node   T3
    #      / \              /   \
    #     T2 T3            T1   T2
    def _leftRotate(self, node):

        x = node.right
        # 左旋转
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = True

        return x

    #      node                   x
    #     /   \     右旋转       /  \
    #    x    T2   ------->   y   node
    #   / \                       /  \
    #  y  T1                     T1  T2
    def _rightRotate(self, node):

        x = node.left
        # 右旋转
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = True

        return x

    def _flipColors(self, node):

        node.color = True
        node.left.color = False
        node.right.color = False

    def add(self, k, v):

        self._root = self._add(self._root, k, v)
        self._root.color = False

    def _add(self, node, k, v):

        if node.key == None:
            self._size += 1
            return Node(k, v, Node(), Node())

        if k < node.key:
            node.left = self._add(node.left, k, v)
        elif k > node.key:
            node.right = self._add(node.right, k, v)
        else:
            node.value = v

        if self.isRed(node.right) and not self.isRed(node.left):
            node = self._leftRotate(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self._rightRotate(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self._flipColors(node)

        return node

    def _getNode(self, node, k):

        if node.key == None:
            return None
        if k == node.key:
            return node
        elif k < node.key:
            return self._getNode(node.left, k)
        else:
            return self._getNode(node.right, k)

    def contains(self, k):
        return self._getNode(self._root, k) != None

    def get(self, k):

        node = self._getNode(self._root, k)
        if node == None:
            return None
        return node.value

    def set(self, k, v):

        node = self._getNode(self._root, k)
        assert node != None, k + "doesn't exist!"
        node.value = v

    def preOrder(self):
        self._preOrder(self._root)

    def _preOrder(self, node):

        if node.key == None:
            return
        print(str(node.key) + ":" + str(node.value))
        self._preOrder(node.left)
        self._preOrder(node.right)

    def findMin(self):
        return self._findMin(self._root).value

    def _findMin(self, node):

        if node.left.key == None:
            return node
        return self._findMin(node.left)

    def removeMin(self):

        assert self._size >= 0, "Can not delete from 0 size!"
        node = self._findMin(self._root)
        self._root = self._removeMin(self._root)

        return node.value

    def _removeMin(self, node):

        if node.left.key == None:
            rightNode = node.right
            node.right = None
            self._size -= 1
            return rightNode
        node.left = self._removeMin(node.left)

        return node

# 测试
if __name__ == "__main__":

    bsm = RBMap()
    bsm.add(1,'k')
    bsm.add(2,2)
    bsm.preOrder()
    print(bsm.findMin())
    print(bsm.removeMin())
    print(bsm.size())
    print(bsm.isEmpty())
    print('-----------------')
    print("success!")



