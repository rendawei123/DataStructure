"""
基于队列实现迷宫问题

框架
将start标记为已达
start入队
while 队列里面有为充分探查的位置
    取出一个位置pos
    检查出pos的相邻
        遇到end成功结束
        尚未探查的都mark并入队
队列空，搜索失败
"""
# 导入队列
from queue import SQueue


# 定义迷宫
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 为了能方便的计算相邻位置，这里定义一个二元组（二元序对）的表，其元素是从位置（i，j）得到四邻位置应该加的数对,对于任何位置，给他加上dir[0],dir[1],dir[2],dir[3],就分别得到了东南西北的四个相邻位置
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 标记位置
def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2

# 检查迷宫maze的位置pos是否可行
def possible(maze, pos):
    return maze[pos[0]][pos[1]] == 0

# 定于基于队列的迷宫算法
def find_path_queue(maze, start, end):
    if start == end:
        print('path find')

    q = SQueue()
    mark(maze, start)
    q.enqueue(start)
    while not q.is_empty():
        pos = q.dequeue()
        for i in range(4):
            next_p = (pos[0]+dirs[i][0], pos[1]+dirs[i][1])
            if possible(maze, next_p):
                if next_p == end:
                    print('path find')
                    return
                mark(maze, next_p)
                q.enqueue(next_p)
    print('no path')


if __name__ == '__main__':
    start = (1, 1)
    end = (10, 12)
    find_path_queue(maze, start, end)
