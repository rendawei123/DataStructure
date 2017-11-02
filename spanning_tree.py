"""
生成树
    1.生成树就是将图从起点开始改造成生成树，我们已将知道了如何实现DFS遍历，剩下的就是如何构造蹦给出所需的DFS生成树，生成树的顶点就是原图的顶点，现在的关键就是设法表示生成树上的边
    2.生成树上的边形成了从初始顶点到其他顶点的一簇路径，在这簇路径里面，一个顶点可能有多个下一顶点，但每个顶点至多有一个‘前一顶点’。记录路径的一种方式是记录所有的“前一顶点”关系，有了这些信息，遍历完所有的顶点之后，根据前一顶点关系就能追溯出所有的路径了。

DFS生成树
    递归
    非递归

BFS生成树

现在考虑递归法构造DFS生成树
"""

def DFS_span_forest(graph):
    vnum = graph.vertex_num()  # 顶点数
    span_forest = [None] * vnum  # 记录所有路径信息

    def dfs(graph, v):
        nonlocal span_forest
        for u, w in graph.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                dfs(graph, u)

    for v in range(vnum):
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            dfs(graph, v)

    return span_forest
