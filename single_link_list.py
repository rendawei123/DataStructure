import random


class LinkedListUnderflow(ValueError):
    """
    手动定义一个异常类，在无结点操作时用于引发
    """
    pass


class LNode:
    """
    定义一个简单的表结点类，其中elem为表元素域，next_为下一结点链接域
    定义为next_主要为避免与Python标准函数next重名
    """
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedList:
    """
    定义单链表类
    """
    # 初始化头结点为None
    def __init__(self):
        self._head = None

    def is_empty(self):   # 判断链表是否为空
        return self._head is None

    def append_head(self, elem):  # 在表头插入数据
        # node = LNode(elem)
        # node.next = self._head
        # self._head = node
        self._head = LNode(elem, self._head)

    def pop_head(self):  # 删除表头
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):  # 在链表的最后插入元素
        # 判断链表是否为空，如果链表为空，则直接将元素赋值给表头
        if self._head is None:
            self._head = LNode(elem)
            # print('empty')
            return

        # 循环遍历出最后一个结点
        p = self._head
        # print(p.elem)
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
        # print(p.next.elem)

    def pop(self):  # 删除表中最后元素操作
        # 先判断链表是否为空，如果为空的话引发异常
        if self._head is None:
            raise LinkedListUnderflow('in pop last')
        # 判断如果链表只有一个结点的话，返回这个结点的值，直接变为空链表
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        # 如果都不是前面两种情况的话，循环遍历找到倒数第二个结点
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def print_all(self):  # 依次遍历打印所有元素
        p = self._head
        while p is not None:
            print('%s ->' % p.elem, end=' ')
            p = p.next
        print(None)

    def filter(self, pre):   # 为链表定义过滤器
        p = self._head
        while p is not None:
            if pre(p.elem):
                yield p.elem
            p = p.next

    def elements(self):  # 定义链表的生成器函数
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next


class LList1(LinkedList):
    """
    原链表如果在尾部添加元素的话需要重新遍历整个链表，影响效率
    通过继承和扩充重新定义链表类，使其加入尾部作用域，方便尾部添加元素
    添加尾部作用域后，凡是涉及到尾部作用域的方法都需要重写
    """
    def __init__(self):
        LinkedList.__init__(self)
        self._rear = None

    def append_head(self, elem):  # 添加头结点
        if self._head is None:  # 链表为空
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):  # 末尾添加结点
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop(self):
        if self._head is None:
            raise UnboundLocalError('empty')
        p = self._head.next
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


def predicate(n):   # 定义功能型函数,过滤小于5的元素
    if n < 5:
        return True
    return False

if __name__ == '__main__':
    # a = LinkedList()
    # print(a.is_empty())
    # a.print_all()
    # for i in range(11):
    #     a.append_head(i)
    # for j in range(11, 20):
    #     a.append_end(j)
    # a.print_all()
    # print(a.pop_head())
    # print(a.pop_last())
    # a.print_all()
    # for i in a.filter(predicate):
    #     print(i)
    b = LList1()
    b.append_head(99)
    for i in range(11, 20):
        b.append(random.randint(1, 20))
    b.print_all()
    for x in b.filter(lambda y: y % 2 == 0):
        print(x)
