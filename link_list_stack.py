"""
本题考虑如何使用连接表实现栈类，名为链接栈

优点：
    1.由于可以自动扩大存储区、基于顺序表的栈类不会出现栈满的情况，可以满足绝大部分的要求，但是扩大存储需要进行一次高代价操作，链表就不需要
    2.顺序表需要完整的大块存储区，链表不需要

缺点：
    更多的依赖于解释器的存储管理，每个节点的链接开销，以及链接结点在实际计算机内存中任意散布可能带来的操作开销

定义
    1，以表头一端作为栈顶，表尾一端作为栈底
"""


class StackUnderflow(ValueError):
    """
    通过继承已有的异常类来定义自己的异常类
    """
    pass


class LNode:
    """
    定义结点类
    """
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LLStack():
    """
    基于连接表实现的栈类，使用LNode作为结点
    """
    def __init__(self):  # 设置表头为栈顶
        self._top = None

    def is_empty(self):   # 如果栈顶元素为None的话，表示为空栈
        return self._top is None

    def top(self):  # 定义返回栈顶元素，如果是空栈，引发异常，否则返回栈顶元素
        if self._top is None:
            raise StackUnderflow('此栈是空栈')
        return self._top.elem

    def push(self, elem):   # 压入元素，在链接表的表头添加创建的新结点
        p = LNode(elem)
        p.next = self._top
        self._top = p

    def pop(self):  # 弹出操作，删除并返回链接表head
        if self._top is None:
            raise StackUnderflow('空栈')
        p = self._top
        self._top = p.next
        return p.elem


if __name__ == '__main__':
    s = LLStack()
    # s.pop()
    s.push(1)
    s.push(2)
    print(s.pop())
