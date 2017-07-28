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

    # 判断链表是否为空，如果头结点为None的话，说明链表为空
    def is_empty(self):
        return self._head is None

    # 在表头插入数据
    def append_head(self, elem):
        # node = LNode(elem)
        # node.next = self._head
        # self._head = node
        self._head = LNode(elem, self._head)

    # 删除表头
    def pop_head(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    # 在链表的最后插入元素
    # 必须要先通过一个扫描循环找到最后一个结点后把包含新元素的结点插入在其后
    def append_end(self, elem):
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

    # 删除表中最后元素操作
    def pop_last(self):
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

    def print_all(self):
        if self._head is None:
            raise LinkedListUnderflow('empty')
        p = self._head
        while p is not None:
            print('%s ->' % p.elem, end=' ')
            p = p.next
        print(None)

if __name__ == '__main__':
    a = LinkedList()
    # a.pop_head()
    # print(a.is_empty())
    # a.append_head(1)
    # print(a.is_empty())
    # print(a.pop_head())
    a.append_end(1)
    a.append_end(2)
    # a.append_end(3)
    # a.append_end(4)
    a.print_all()
    print(a.pop_last())
    print(a.pop_last())
    # print(a.pop_last())