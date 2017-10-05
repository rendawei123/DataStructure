"""
背包问题（动态规划）：
    一个背包里可仿佛重量为weight的物品，现有n件物品的集合S，其中物品的重量分别为w0，w1...wn,
    问题是，能否从中选出若干物品，其重量之和正好等于weight。
    如果存在，就说这一背包问题有解，否则就无解

问题求解
    假设背包重量为weight，w_list为物品的重量列表，n为物品的数量
    此问题可以使用递归分治思想类解
    这个问题可以分为两个小问题来求解
        1、如果选最后一件物品，这时如果bag(weight-w_list, n-1)有解的话，这个问题就有解，否则为false
        2、如果不选最后一件物品，这时如果bag(weight, n-1)有解的话，这个问题就有解，否则是false
    这样，问题又转化为更小的bag(weight-w_list, n-1)的问题以及bag(weight, n-1)的问题，这样依次类推，最后可以转化为剩一个进行判断，就很好判断来
"""

def bag(weight, w_list, n):
    if weight == 0:
        return True
    if weight < 0 or (weight>0 and n<1):
        return False
    if bag((weight - w_list[n-1]), w_list, n-1):
        return True
    if bag(weight, w_list, n-1):
        return True
    else:
        return False


if __name__ == '__main__':
    weight = 5
    w_list = [1, 2, 3]
    n = 2
    print(bag(weight, w_list, n))
