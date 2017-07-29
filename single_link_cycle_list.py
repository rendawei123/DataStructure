class LinkedListUnderflow(ValueError):
    """
    自定义一个错误，用于引发链表异常
    """
    pass


class LNode:
    """
    定义结点类
    """
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LCList:
    """
    定义循环单链表，循环单链表其实就是将尾端的链接域指向链表头
    定义循环单链表记录尾结点更加方便
    """
    def __init__(self):
        self._rear = None

    def is_empty(self):  # 判断链表是否为空
        return self._rear is None

    def append_head(self, elem):  # 链表头加入结点
        p = LNode(elem)
        if self._rear is None:
            p.next = p  # 建立一个结点的环
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.append_head(elem)
        self._rear = self._rear.next

    def pop_head(self):  # 弹出链表头
        if self._rear is None:
            raise LinkedListUnderflow('in pop of CLList')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def print_all(self):
        if self._rear is None:
            return
        p = self._rear.next
        while True:
            print(p.elem, end=' ')
            if p is self._rear:
                break
            p = p.next
        print()


if __name__ == '__main__':
    a = LCList()
    a.append_head(1)
    a.append(2)
    # print(a.is_empty())
    a.print_all()
    print(a.pop_head())
    print(a.pop_head())
    a.print_all()
