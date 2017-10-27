"""
堆

首先分析连续表实现的优先队列效率低的原因：

按序插入插入效率低，其根源是其根源就是需要沿着表顺序检索插入位置，表长度是n，表长度为n的话，检索必然需要O(n)时间，这说明，只要元素按优先级顺序线性排列，就无法避免线性复杂性问题，
对于顺序表需要移动O(n)个元素，对于链表，需要顺着链接爬行O(n)步
这些情况意味着，如果不改变数据的线性顺序存储方式，就不可能突破O(n)的复杂度限制，要作出效率更高的优先队列，必须考虑其他数据结构组织方式

采用树形结构实现优先队列的一种有效技术成为堆，
堆就是结点里存储数据的完全二叉树
但是堆中数据的存储需要满足一种特殊堆序：任何一个结点里所存的数据先于或等于其子结点里的数据

性质：
1.在一个堆中从树根到任何一个叶结点的路径上，各结点里所存的数据按规定的优先关系（非严格）递减
2.堆中最优先的元素必定位于二叉树的跟结点里，O(1)时间就能找到
3.位于树中不同路径上的元素，这里不关心其顺序关系

堆与优先队列
基于堆构建优先队列需要解决两个问题：
1.如何实现插入元素的操作，向堆中加入了一个新元素，必须能通过操作，得到一个包含了所有原有元素和刚加入的新元素的堆
    解决：
    在一个堆中加入一个元素，得到的结果还可以看作完全二叉树，但未必是堆，为把这样的完全二叉树恢复为堆，只需要做一次向上筛选操作
    向上筛选操作：
    不断用新加入的元素e与其父节点的数据比较，如果e较小就交换连个元素的位置，通过这样比较和交换，元素e不断上移，这一操作一直做到e的父节点的数据小于等于e，或者e已经达到跟结点时停止，且整个结构已经恢复为一个堆

2.如何实现弹出元素的操作：从堆中弹出最小元素后，必须要把剩余元素重新做成堆
    解决：
    由于堆顶元素就是最优元素，应该弹出的就是他，但是弹出堆顶元素后，剩下的元素已经不再是堆，而是两个子堆，这时，需要进行如下操作：
        弹出当时的堆顶
        从堆最后取出一个元素作为完全二叉树的根
        执行一次向下筛选
    向下筛选：
    假设e与A、B两个子堆的堆顶元素比较，最小者作为整个堆的顶
    如果e不是最小，最小的必定是A或者B的根，假设是A的根，将其移动到堆顶，相当于删掉了A的顶元素
    然后把e放入去掉堆顶的A，这就变成了规模更小的同一问题
    如果某次比较中e最小，以他为顶的局部树已经成为堆，整个结构也就成为堆，
    或者e已经落到底，这时他自身就是一个堆，整个结构也成为堆

3.如何将一个列表构建成一个堆
    解决：
    一个元素的序列已经是堆
    如果元素位置合适，在表里面已经有两个子堆上加一个元素，通过一次向下筛选，就可以把这部分元素调整为一个更大的子堆
    把初始的表看作一颗完全二叉树，从下标end//2的位置开始，后面的表元素都是二叉树的叶结点，也就是说，他们中的每一个已经是一个堆，从这里开始往前做，也就是说，从完全二叉树的最下最右分支结点开始，向左一个个建堆，然后再到上一层建堆，直到整个表建成一个堆
"""
from priority_queue_list import PriorityQueueError

# 基于堆的优先队列类
class PriorityQueueHeap:
    """基于堆实现优先队列"""
    def __init__(self, elist=[]):  # 注意，这里在函数中的参数如果是一个列表，会共享
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PriorityQueueError('in peek')
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems)-1)

    def siftup(self, e, last):
        # 对于完全二叉树，对于任意一结点i，都有对于i>0，其父节点的编号为(i-1)/2
        elems, i, j = self._elems, last, (last-1)//2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PriorityQueueError('in dequeue')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j*2+1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)

if __name__ == '__main__':
    # q = PriorityQueueHeap([8,3,7,4,5,9,4,3,0])
    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.dequeue())
    q = PriorityQueueHeap()
    q.enqueue(3)
    q.enqueue(2)
    print(q.dequeue())
