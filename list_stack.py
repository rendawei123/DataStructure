# 由于栈是一个特殊的线性表，所以可以基于顺序表实现实现栈的功能
# 建立空栈对应于创建一个空表[]，判断是否为空栈对应于检查是否为空表
# 由于list采用动态顺序表技术，（分离式实现）作为栈的表不会满
# 压入元素操作应该在表的尾端进行，对应于list.append(x)
# 访问栈顶元素应该用list(-1)来进行
# 弹出操作也应该在表的尾端进行，对应于list.pop()默认弹出表尾元素

class StackUnderflow(ValueError):
    """定义栈溢出错误"""
    pass

class ListStack(object):
    """使用顺序表实现栈"""
    def __init__(self):
        self._elems == []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow('empty')
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow('empty')
        return self._elems.pop()
