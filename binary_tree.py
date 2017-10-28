"""
定义二叉树
下面定义二叉树的list表现形式,它实现了基本的操作
"""


def binary_tree(data, left=None, right=None):
    return [data, left, right]

def is_empty_binary_tree(btree):
    return btree is None

def root(btree):
    return btree[0]

def left(btree):
    return btree[1]

def right(btree):
    return btree[2]

def set_root(btree, data):
    btree[0] = data

def set_left(btree, left):
    btree[1] = left

def set_right(btree, right):
    btree[2] = right


"""
二叉树的类实现：

由于二叉树由一组结点组成，现在定义一个表示二叉树结点的类，结点通过链接引用其子结点，
没有结点时用None表示
"""

class BinTreeNode:
    """
    定义二叉树的结点类
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 统计树中结点个数,递归
def count_BinTreeNode(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTreeNode(t.left) + count_BinTreeNode(t.right)

# 假设结点中保存数值，求这种二叉树里的所有数值和，递归
def sum_BinTreeNode(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTreeNode(t.left) + sum_BinTreeNode(t.right)

"""
二叉树类

直接基于结点构造的二叉树具有递归的性质，可以很方便的处理，但这样的二叉树结构也有不统一之处
其中用None表示空树，但是，None的类型并不是BinTreeNode,
另外，基于二叉树结点构造的结构，并不是一种良好封装的抽象数据类型

解决这些问题的方法就是定义一个二叉树类，以前面定义的BinTreeNode结点链接而成的树形结构作为其内部表示
"""

from list_stack import ListStack

class BinTree(object):
    """定义二叉树类"""
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def root(self):
        return self._root

    def left_child(self):
        return self._root.left

    def right_child(self):
        return self._root.right

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self._root.right = rightchild

    # 定义一个元素迭代器,后根序遍历二叉树
    def preorder_elements(self):
        t, s = self._root, ListStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data

                t = t.left
            t = s.pop()





if __name__ == '__main__':
    t = BinTreeNode(1, BinTreeNode(2), BinTreeNode(3))
    print(count_BinTreeNode(t))
    print(sum_BinTreeNode(t))
