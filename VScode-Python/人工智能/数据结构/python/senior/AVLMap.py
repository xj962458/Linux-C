'''
                    --  用AVL平衡树实现映射  --

        此版本的缺陷是，key键只能为数字，value可以为任何数据类型的

        Node类：
            初始化一个节点

        AVLMap类：

            size：       返回映射长度
            isEmpty：    判断映射是否为空
            _getHeight： 得到当前节点高度
            _getBalanceFactor：得到平衡因子
            isBalanced： 判断是否为一个平衡二叉树
            _rightRotate：右旋转
            _leftRotate：左旋转
            _getNode：   辅助函数，用来得到树中key键对应的的节点Node，若key不存在，则返回None
            add：        增加一组键值对
            contains：   看是否包含键值对key-value
            set：        重新设置value值，不存在键key即返回报错信息
            get：        得到key对应的值
            remove：     删除一组键值对
            preOrder：   输出映射中所有的键值对

        Made by JinFan  -- 2019.09.27
'''





class Node:

    def __init__(self, key=None, value=None, left_=None, right_=None):

        self.key = key
        self.value = value
        self.left = left_
        self.right = right_
        self.height = 1

class AVLMap:

    def __init__(self):
        self._root = Node(None, None, Node(), Node())
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def _getHeight(self, node):

        if node == None:
            return 0
        return node.height

    def _getBalanceFactor(self, node):

        if node.key == None:
            return 0
        return self._getHeight(node.left) - self._getHeight(node.right)

    def isBalanced(self):
        return self._isBalanced(self._root)

    def _isBalanced(self, node):

        if node.key == None:
            return True
        balanceFactor = self._getBalanceFactor(node)

        if abs(balanceFactor) > 1:
            return False

        return self._isBalanced(node.left) and self._isBalanced(node.right)

    #  对节点y进行向右旋转操作，返回旋转后新的根节点x
    #         y                              x
    #        / \                           /   \
    #       x   T4     向右旋转 (y)        z     y
    #      / \       - - - - - - - ->    / \   / \
    #     z   T3                       T1  T2 T3 T4
    #    / \
    #  T1   T2

    def _rightRotate(self, node):

        x = node.left
        T3 = x.right

        # 向右旋转过程
        x.right = node
        node.left = T3

        # 更新height
        node.height = max(self._getHeight(node.left), self._getHeight(node.right) + 1)
        x.height = max(self._getHeight(x.left), self._getHeight(x.right) + 1)

        return x

    # 对节点y进行向左旋转操作，返回旋转后新的根节点x
    #    y                             x
    #  /  \                          /   \
    # T1   x      向左旋转 (y)       y     z
    #     / \   - - - - - - - ->   / \   / \
    #   T2  z                     T1 T2 T3 T4
    #      / \
    #     T3 T4

    def _leftRotate(self, node):

        x = node.right
        T2 = x.left

        # 向左旋转过程
        x.left = node
        node.right = T2

        # 更新height
        node.height = max(self._getHeight(node.left), self._getHeight(node.right) + 1)
        x.height = max(self._getHeight(x.left), self._getHeight(x.right) + 1)

        return x

    def add(self, k, v):
        self._root = self._add(self._root, k, v)

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

        # 更新height
        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))

        # 计算平衡因子
        balanceFactor = self._getBalanceFactor(node)

        # 平衡维护
        if balanceFactor > 1 and self._getBalanceFactor(node.left) >= 0:
            return self._rightRotate(node)
        if balanceFactor < -1 and self._getBalanceFactor(node.right) <= 0:
            return self._leftRotate(node)
        if balanceFactor > 1 and self._getBalanceFactor(node.left) < 0:
            node.left = self._leftRotate(node.left)
            return self._rightRotate(node)
        if balanceFactor < -1 and self._getBalanceFactor(node.right) > 0:
            node.right = self._rightRotate(node.right)
            return self._leftRotate(node)

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

    def preOrder(self):
        self._preOrder(self._root)

    def _preOrder(self, node):

        if node.key == None:
            return
        print(str(node.key) + ":" + str(node.value))
        self._preOrder(node.left)
        self._preOrder(node.right)

    def remove(self, k):

        node = self._getNode(self._root, k)
        if node != None:
            self._root = self._remove(self._root, k)
            return node.value
        return None

    def _remove(self, node, k):

        global retNode
        if node.key == None:
            return None
        if k < node.key:
            node.left = self._remove(node.left, k)
            retNode = node
        elif k > node.key:
            node.right = self._remove(node.right, k)
            retNode = node
        else:
            if node.left.key == None:
                rightNode = node.right
                # node.right = None
                self._size -= 1
                retNode = rightNode
            elif node.right.key == None:
                leftNode = node.left
                node.left = None
                self._size -= 1
                retNode = leftNode
            else:

                successor = self._findMin(node.right)
                successor.right = self._remove(node.right, successor.key)
                successor.left = node.left
                node.left = node.right = None

                retNode = successor

        if retNode == None:
            return None

        # 更新height
        retNode.height = 1 + max(self._getHeight(retNode.left), self._getHeight(retNode.right))

        # 计算平衡因子
        balanceFactor = self._getBalanceFactor(retNode)

        # 平衡维护
        if balanceFactor > 1 and self._getBalanceFactor(retNode.left) >= 0:
            return self._rightRotate(retNode)
        if balanceFactor < -1 and self._getBalanceFactor(retNode.right) <= 0:
            return self._leftRotate(retNode)
        if balanceFactor > 1 and self._getBalanceFactor(retNode.left) < 0:
            retNode.left = self._leftRotate(retNode.left)
            return self._rightRotate(retNode)
        if balanceFactor < -1 and self._getBalanceFactor(retNode.right) > 0:
            retNode.right = self._rightRotate(retNode.right)
            return self._leftRotate(retNode)

        return retNode


# 测试
if __name__ == "__main__":

    bsm = AVLMap()
    bsm.add(1,'k')
    bsm.add(2,2)
    bsm.preOrder()
    bsm.remove(3)
    bsm.remove(2)
    print(bsm.size())
    print(bsm.isEmpty())
    print(bsm.isBalanced())
    print('-----------------')
    print("success!")






