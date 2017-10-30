"""
哈夫曼二叉树树

给定n个权值作为n个叶子结点，构造一棵二叉树，若带权路径长度达到最小，称这样的二叉树为最优二叉树，也称为哈夫曼树(Huffman Tree)。哈夫曼树是带权路径长度最短的树，权值较大的结点离根较近。

构造哈夫曼树的算法

哈夫曼提出了一个算法，它能从任意的时数集合构造出与之对应的哈夫曼树。这个构造算法描述如下：
    1，算法的输入为实数集 W = {w0, w1,...w(m-1)}
    2，在构造中维护一个包含k颗二叉树的集合F，开始时k=m,且F={T0,T1,...T(m-1)},其中每个T1是一颗只包含权为w(i)的跟结点的单点二叉树。
    3,算法过程中重复执行下面两个步骤，直到集合F中剩下一棵树为止
        a:构造一颗新的二叉树，其左右子树是从集合F中选取的两颗权最小的二叉树，其根结点的权值设置为这两颗子树的根节点的权值之和
        b:将所选的两颗二叉树从F中删除，把新构造的二叉树加入F，这个步骤每做一次，F里的二叉树就减少了一颗，这就保证了本算法必定结束

如何实现

显然，构造算法执行中需要维护一组二叉树，而且要直到每棵树（其树根结点）的权值，可以考虑使用二叉树的结点类构造哈夫曼树，在树根结点记录树的权值。

在算法执行过程中需要不断选出权值最小的两颗二叉树， 并基于他们构造出一颗新的二叉树，很容易想到，我们需要最佳的选择就是用优先队列存放这组二叉树，按照二叉树的跟结点的权值排列优先顺序，从小到大

算法开始时建立起一组单结点的二叉树，以权值作为优先码存入优先队列，要求先取出队列里的最小元素，然后反复做下面的事情
        1，从优先队列里面弹出两个权值最小的元素（两颗二叉树）
        2，基于所取的二叉树构造一颗新的二叉树，其权值取两颗子树权值之和，并向构造的新二叉树压入优先队列

需要解决的问题：
    1.需要为二叉树定义一个序，权值小的二叉树在前，
    2。需要检查优先队列中的元素个数，以便在剩一颗时结束，这些都可以通过扩充前面已经定义的类型实现

应用：哈夫曼编码
"""

from binary_tree import BinTreeNode
from priority_queue_list import PriorityQueue

# 以二叉树结点类作为基类，定义一个专门为构造哈夫曼树用的结点类，其特点是怎加一个小于比较操作符
class HaffmanNode(BinTreeNode):
    def __lt__(self, othernode):
        return self.data < othernode.data

# 定义一个专门为哈夫曼算法服务的优先队列类，增加了一个检查队列中元素个数的方法
class HuffmanPriorityQueue(PriorityQueue):
    def number(self):
        return len(self._elems)

# 定义哈夫曼树
def HuffmanTree(weights):
    trees = HuffmanPriorityQueue()  # 实例化优先队列

    for w in weights:  # 将每个权重构造成单点二叉树，然后全部加入优先队列
        each_tree = HaffmanNode(i)
        trees.enqueue(each_tree)

    while trees.number() > 1:    # 直到队列中只剩下一个树，就是哈夫曼树
        t1 = trees.dequeue()
        t2 = trees.dequeue()  # 取出最小的两棵树
        x = t1.data + t2.data  # 得到新树的权重
        new_tree = HaffmanNode(x, t1, t2)  # 构造新树
        trees.enqueue(new_tree)   # 将新树加入优先队列

    return trees.dequeue()
