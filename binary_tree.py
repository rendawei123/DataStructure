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
