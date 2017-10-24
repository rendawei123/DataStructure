"""
基于线性表实现的优先队列

作为缓存结构，优先队列与栈和队列类似，可以将数据元素保存其中，可以访问和弹出，
优先队列的特点是存入其中的每一项数据都另外附有一个数值，表示这个项的优先程度

对连续表实现的分析

现在分析这一实现中各操作的效率，插入元素是O(n),其他都是O(1)操作，即使插入时表的存储区满，需要换一块存储，复杂度量级也没有变，仍然是O(n)
"""

# 首先定义一个异常类
class PriorityQueueError(ValueError):
    pass

# 使用列表将优先队列定义为一个类
class PriorityQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)   # 传入的列表里面为一个个的二元组
        self._elems.sort(reverse=True)   # 使所有的二元组按照优先级进行排序，


    # 插入元素的时候必须保证传入元组的第一个元素，也就是优先级插入到合适的位置
    def enqueue(self, e):   # 这里传入的e为一个二元组，第一个为优先级，第二个为值
        i = len(self._elems) - 1   # 从末尾往前遍历，寻找到合适的位置插入
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PriorityQueueError('in pop')
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PriorityQueueError('in pop')
        return self._elems.pop()


if __name__ == '__main__':
    q = PriorityQueue()
    q.enqueue((4,2))
    q.enqueue((3,8))
    print(q.dequeue())
