"""
队列（queue）
    队列中没有位置的概念，只支持默认方式的存入和取出
特点：
    队列是一个封闭集合
    可以保证在任何时间可访问和删除元素的元素都是在此之前最早存入而未删除的元素
    队列是一个先进先出的结构
队列的基本操作：
    创建新队列对象
    判断队列是会否为空
    将一个元素放入队列
    从队列中删除元素并返回他
    查看队列里当前（最老的）元素

队列的实现：
    连接表实现：
    由于队列的特点和链表非常像，就是尾部操作传统的链表可能无法实现，但是，我们可以直接使用带有尾指针的链表来实现
    顺序表实现：
    1.顺序表实现的时候尾端插入可以很方便的实现，但是首端出队操作之后，全部元素都要前移

队列结构要求：
    1、多有构造对象的操作，都必须吧对象成分设置为满足数据不变式的状态，也就是说，对象的初始状态应该满足数据不变式
    2、每个对象操作都应该保证不破坏数据不变式
    3、_elems属性引用着元素的存储区，他是一个list对象，_len属性记录着存储区的有效容量，（由于python语言的特性，无法获知list对象的实际大小）
    4、_head是队列中首元素（最早存入元素）的下标，_num始终记录着队列元素的个数
    5、当队列里的元素总保存在_elems里从_head里开始的连续位置中，新入队的元素存入_head+_num算出的位置，但是如果 需要把元素存入下标_len的位置时，改为在下标0位置存入该元素
    6、在_num==_len的情况下出现入队操作，就扩大存储区
描述：
    使用链表和顺序表描述描述队列比较简单，应为他们会自动的扩大内存空间，不会出现队列满的情况，
    但是使用数组就比较麻烦，因为使用数组的话有可能造成队列满的情况，
    这种情况就需要靠取模以及手动扩大内存来满足
"""
# 首先，队列可能因为空而无法完成出队操作等，为此定义一个异常
class QueueUnderflow(ValueError):
    pass


# 队列类的实现
class SQueue():
    """队列类的实现 """
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0

    def is_empty(self):  #判断队列是否为空
        return self._num == 0

    def peek(self):  # 取得队列首元素
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]

    # 出队操作，取得队列首元素后修改_head属性的值以及self.num
    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head+1) % self._len
        self._num -= 1
        return e

    # 入队操作，必须要先进行判断，如果队列满的话，必须要扩大
    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()    # 扩大队列空间
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1

    # 扩大队列空间
    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % self._len]
        self._elems, self._head = new_elems, 0
