"""
树的遍历

树的遍历有两种形式，一种是深度优先、一种是宽度优先
树的遍历有两种算法，一种是递归，一种是非递归
"""

from binary_tree import BinTreeNode

# 定义结点数据操作函数
def print_data(data):
    print(data)

"""
递归深度优先遍历

这种遍历的顺序深度优先
根结点---左子树---右子树
"""

def preorder(t, proc):
    if t is None:
        return
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)


"""
递归宽度优先遍历

要实现采用宽度优先遍历二叉树，首先需要一个队列，
"""

from queue import SQueue

def levelorder(t, proc):
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        n = qu.dequeue()
        if n is None:  # 如果弹出的树为空的话，直接跳过
            continue
        qu.enqueue(n.left)
        qu.enqueue(n.right)
        proc(n.data)


"""
非递归的先根序遍历

下面讨论非递归定义的深度优先遍历算法，
由于采取先根序，遇到结点时就应该访问，下一步就应该沿着树的左分支下行
但结点的右分支还没有访问，因此需要记录，将右子结点入栈
遇到空树时回溯，取出栈中保存的一个右分支，向一颗二叉树一样遍历它
"""

from list_stack import ListStack

def preorder_non_recursion(t, proc):
    s = ListStack()
    while t is not None or not s.is_empty():
        while t is not None:
            proc(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()

"""
通过生成器函数遍历
"""

def preorder_non_recursion_elements(t):
    s = ListStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()

"""
非递归的中根序遍历
"""

def midorder_non_recursion(t, proc):
    s = ListStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left
        t = s.pop()
        proc(t.data)
        t = t.right



"""
非递归的后根序遍历

栈中结点序列的左边是二叉树已经遍历的部分，右边是尚未遍历的部分
如果不为空，其父节点就是栈顶结点
t空时栈顶就是应访问的结点
"""

def postorder_non_recursion(t, proc):
    s = ListStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left is not None else t.right
        t = s.pop()
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None



if __name__ == '__main__':
    t = BinTreeNode(1, BinTreeNode(2, BinTreeNode(4), BinTreeNode(5)), BinTreeNode(3))
    # preorder(t, print_data)
    # levelorder(t, print_data)
    # preorder_non_recursion(t, print_data)
    midorder_non_recursion(t, print_data)
    # postorder_non_recursion(t, print_data)
