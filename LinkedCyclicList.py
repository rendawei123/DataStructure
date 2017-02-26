class LinkedListUnderflow(ValueError):
    pass


class LinkedNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedCyclicList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LinkedNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow('in pop of CyclicLinkedList')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def print_all(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem, end=' ')
            if p is self._rear:
                break
            p = p.next
        print('')


def test():
    list1 = LinkedCyclicList()
    for i in range(6):
        list1.append(i)
    list1.print_all()
    for i in range(6, 11):
        list1.prepend(i)
    list1.print_all()

if __name__ == '__main__':
    test()