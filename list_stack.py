"""
由于栈是一个特殊的线性表，所以可以基于顺序表实现实现栈的功能
建立空栈对应于创建一个空表[]，判断是否为空栈对应于检查是否为空表
由于list采用动态顺序表技术，（分离式实现）作为栈的表不会满
压入元素操作应该在表的尾端进行，对应于list.append(x)
访问栈顶元素应该用list(-1)来进行
弹出操作也应该在表的尾端进行，对应于list.pop()默认弹出表尾元素

缺点：
    1.扩大存储区需做一次高代价操作，如果采用简单的顺序表实现，会出现栈满的情况，继续压入元素可能会溢出，如果采用动态顺序表，栈满之后会自动换一块大的存储区，这种情况又会出现存储区的置换策略问题以及分期付款式的的O（1）时间复杂度问题
    2.顺序表需要完整的大块存储区
    3.采用顺序表式依托list构建的，这样建立的对象还是list，提供类list类型的所有操作，特别式提供类一大批栈结构原本不应该支持的操作，威胁栈的安全性。
    4.这样构建的栈不是一个独立类型，因此没有独立类型的所有重要性质
"""

class StackUnderflow(ValueError):
    """定义栈溢出错误"""
    pass

class ListStack(object):
    """使用顺序表实现栈"""
    def __init__(self):
        self._elems = []

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



if __name__ == '__main__':
    a = ListStack()
    a.push(1)
    print(a.pop())
