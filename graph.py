"""
图：

在python里面实现图结构有以下几种方法

1.以list为元素的list(两层的表)或者tuple的tuple（两层的tuple）结构作为邻接矩阵的直接实现来表示图结构，这种表示方法结构简单，使用也很方便，容易判断定点的邻接关系。但存储代价较大，不适合很大的图

2.定义一种字典，以顶点的下标序对（i, j)作为关键码，实现从顶点对到邻接关系的映射，优点是检索效率很高，采用适当技术，可以做到图的空间开销与图中边数成正比，适合表示稀疏矩阵，但python的字典本身比较复杂，而且基于顺序存储实现，是否适合大型图需要实验

3.用python内置的bytearray字节向量类型或者标准库的array类型。bytearray是内置类型，与str类似，但为可变类型。bytearray对象的元素是二进制字节，可以用于表示边的存在与否，存储效率高，array是标准库里面定义的数值汇集类型，其对象的元素可以是整数或者浮点数等基本类型值，可用于表示带权图。

4.自定义类型实现邻接表表示，其中具体数据的组织可以考虑上述各种技术

下面讨论两种自定义的实现方法--邻接矩阵实现和邻接表实现
"""

# 定义无穷大
inf = float("inf")

# 图的邻接矩阵实现
class Graph:
    def __init__(self, mat, unconn=0):
        vnum = len(mat)   # 表示有几列
        for x in mat:
            if len(x) != vnum:   # 检查是否为方阵,每一行是否为列数
                raise ValueError('Argument for Graph')
        self._mat = [mat[i][:] for i in range(vnum)]  # 拷贝
        self._unconn = unconn
        self._vnum = vnum  # 顶点个数

    def vertex_num(self):   # 顶点数
        return self._vnum

    def _invalid(self, v):  # 判断顶点v是否是有效顶点
        return 0 > v or v >= self._vnum

    def add_vertex(self):   # 不支持增加顶点
        raise ValueError('do not support')

    def add_edge(self, vi, vj, val=1):  # 添加边，必须要检查顶点下标的合法性
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + 'or' + str(vj) + 'is not a valid vertex')
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):  # 找出边，也必须要检查顶点下标的合法性
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + 'or' + str(vj) + 'is not a valid vertex')
        return self._mat[vi][vj]

    def out_edges(self, vi):  # 求顶点的出边
        if self._invalid[vi]:  # 判断顶点是否有效
            raise ValueError(str(vi) + 'is not a valid vertex')
        return self._out_edges(self, _mat)

    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):  # 循环所顶点的那一行，就可以获取边信息
            if row[i] != unconn:  # 如果不是0的话，就说明有边，如果是零的话，说明没有边
                edges.append((i, row[i]))
        return edges

    def __str__(self):
        return "[\n" + ",\n".join(map(str,self._mat)) + "\n]" + "\nUnconnected:" + str(self._unconn)

"""
压缩的邻接矩阵（邻接表）实现

邻接矩阵的缺点是空间占用与顶点数的平方成正比，可能带来很大的浪费，
另外，邻接矩阵不容易实现增加顶点，不太适合以逐步扩充的方式构造图对象

邻接表实现的优点

每个顶点v的所有临接边用一个（不一定等长）的list对象表示，元素形式为（v',w）,其中v'是边的终点，w是边的信息。一个图对象的主要部分就是这种list的list，每个元素对应一个顶点

这种设计很容易给已有的图添加顶点。为此只需要在外层表中增加一个表示新顶点的项，对应的边表设置为空表，通过随后的操作加入边

这种表示能更好地支持以逐步扩充的方式构造大型图对象
"""

class GraphAdjoining(Graph):
    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)  # 顶点数
        for x in mat:  # 判断是否为方阵
            if len(x) != vnum:
                raise ValueError("Argument for 'Graph'")

        # 由于参数是列表复制一份
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
        self._vnum = vnum  # 顶点数
        self._unconn = unconn  # 边数

    # 增加新结点
    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1  # 返回一个新编号

    # 添加一个边
    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0: # 如果顶点数为零
            raise ValueError('Can not add edge to empty Graph')

        if self._invalid(vi) or self._invalid(vj):  # 如果顶点无意义
            raise ValueError(str(vi) + 'or' + str(vj) + 'is not valid vertex')

        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:  # 如果有边，重新赋值
                self._mat[vi][i] = (vi, val)
                return
            if row[i][0] > vj:
                break
            i += 1

        self._mat[vi].insert(i, (vj, val))

    # 获取边
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):  # 如果顶点无意义
            raise ValueError(str(vi) + 'or' + str(vj) + 'is not valid vertex')

        for i, val in self._mat[vi]:
            if i == vi:
                return val

        return self._unconn

    # 获取出边
    def out_edges(self, vi):
        if self._invalid(vi):  # 如果顶点无意义
            raise ValueError(str(vi) + 'is not valid vertex')

        return self._mat[vi]


if __name__ == '__main__':
    # a = [
    # [0,0,0,0,0],
    # [0,0,0,0,0],
    # [0,0,0,0,0],
    # [0,0,0,0,0],
    # [0,0,0,0,0]
    # ]

    # g = Graph(a)
    # print(str(g))
    b = GraphAdjoining()
    b.add_vertex()
    b.add_vertex()
    b.add_edge(0,1)
    b.add_edge(1,0)
    print(str(b))
