"""
图的遍历

深度优先遍历(DepthFirstSearch)
    1.首先访问顶点v，标记为已访问
    2.检查v的邻接顶点，从中选一个尚未访问的顶点，从它出发继续进行深度优先搜索（递归），不存在这种邻接顶点时回溯（邻接顶点可能排了一种顺序）。
    3.反复上述操作直到从v出发可达的所有顶点都已访问（递归）。
    4.如果图中还存在未访问的顶点，则选出一个未访问顶点，由它出发重复前述过程，直到图中所有顶点都已访问为止

宽度优先遍历(BreadthFirstSearch)
    1.先访问顶点vi并将其标记为已访问
    2.依次访问vi的所有相邻顶点v(i-1),v(i-2),v(i-3),v(i-4),再依次访问与v(i-1),v(i-2),v(i-3),v(i-4),邻接的所有尚未访问过的顶点...如此进行下去直到所有可达顶点都已经访问
    3.如果图中还存在未访问顶点，则选择一个未访问顶点，由它出发按照同样方式基于宽度优先搜索工作，直到所有顶点都已访问为止。

下面介绍深度优先遍历的非递归算法
    1.使用栈作为缓存
    2.防止多次遍历同一顶点，我们采用了一个内部的表对象记录访问历史，对应每个顶点都有一个表元素，当一个顶点被访问时，将该顶点下标对应的表元素设置为1，初始时这个表的所有元素取0值
"""
from graph import GraphAdjoining
from link_list_stack import LLStack


def dts_graph(graph, v0):
    vnum = graph.vertex_num()  # 获取顶点数
    visited = [0] * visited  # 创建visited记录所有访问过的顶点
    visited[v0] = 1  # 首先将跟结点记录
    DFS_sqe = [v0]
    st = LLStack()
    st.push((0, graph.out_edges(v0)))  # 将根结点的所有边入栈

    while not st.is_empty():
        i, edges = st.pop()  # (0, graph.out_edges(v0))
        if i < len(edges):
            v, e = edges[i]  # 获取下一个

            st.push((i+1, edges))  # 将edges[i+1]入栈

            if not visited[v]:  # 如果下一个未访问过，将其入栈，继续
                DFS_sqe.append(v)
                visited[v] = 1
                st.push((0,graph.out_edges(v)))

    return DFS_sqe
