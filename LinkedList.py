class LinkedNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LinkedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LinkedNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LinkedNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LinkedNode(elem)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, predicate):
        p = self._head
        while p is not None:
            if predicate(p.elem):
                return p.elem
            p = p.next

    def filter(self, predicate):
        p = self._head
        while p is not None:
            if predicate(p.elem):
                yield p.elem
            p = p.next

    def print_all(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    def for_each(self, process):
        p = self._head
        while p is not None:
            process(p.elem)
            p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next


def predicate_judge(x):
    if 5 <= x <= 15:
        return True
    else:
        return False


def process_add_one(x):
    print(x + 10)


def test():
    l1 = LinkedList()
    for i in range(5):
        l1.prepend(i)
    for i in range(5, 10):
        l1.append(i)
    l1.print_all()
    print(l1.find(predicate_judge))
    print(l1.pop())
    l1.print_all()
    print(l1.pop_last())
    l1.print_all()
    l1.for_each(process_add_one)
    l1.print_all()
    for x in l1.elements():
        print(x, end=' ')
    print('')
    for x in l1.filter(predicate_judge):
        print(x, end=' ')
    print('')

if __name__ == '__main__':
    test()