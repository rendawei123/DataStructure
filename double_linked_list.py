class DoubleLinkedListUnderflow(TypeError):
    """定义异常类"""
    pass


class DLNode:
    """
    定义双链表的结点类
    prev为双链表的前一结点作用域
    next_为爽链表的后一结点作用域
    """
    def __init__(self, elem, prev=None, next_=None):
        self.elem = elem
        self.prev = prev
        self.next = next_


class DoubleLinkedList:
    """
    定义双链表类，爽链表不仅需要头结点，还要指定尾结点
    """
    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):  # 判断是否为空链表
        return self._head is None

    def prepend(self, elem):  # 添加链表头
        p = DLNode(elem)  # 创建一个新结点
        p.next = self._head  # 将新结点的下一个链接域指向表头
        p.prev = None  # 由于新结点要作为表头，将新结点的上一个作用域为空
        if self._head is None:
            self._rear = p  # 如果链接表为空，链表的尾指针和头指针都是p
        else:  # 如果非空，设置prev引用
            p.next.prev = p
        self._head = p

    def append(self, elem):  # 从表尾添加元素
        p = DLNode(elem)
        p.next = None
        p.prev = self._rear
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop_head(self):  # 删除链表头
        if self._head is None:
            raise DoubleLinkedListUnderflow('empty')
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop(self):  # 删除链表尾
        if self._head is None:
            raise DoubleLinkedListUnderflow('empty')
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e

    def print_all(self):  # 打印所有链表元素
        if self.is_empty():
            return
        p = self._head
        while p is not None:
            print(p.elem, end=' ')
            p = p.next
        print()


if __name__ == '__main__':
    a = DoubleLinkedList()
    print(a.is_empty())
    a.prepend(1)
    a.prepend(2)
    a.prepend(3)
    a.print_all()
    print(a.pop_head())
    a.print_all()
    print(a.pop())
    a.print_all()

