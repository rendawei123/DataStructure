class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right


def print_binary_tree(root):
    if root is None:
        print('^', end='')
        return
    print('(' + str(root.value), end='')
    print_binary_tree(root.left)
    print_binary_tree(root.right)
    print(')', end='')

if __name__ == '__main__':
    t = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(5)), BinaryTreeNode(3))
    print_binary_tree(t)
    