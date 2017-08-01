# Josn问题和基于"数组"概念的解法
# 题意：
#   假设有n个人围坐一圈，现在要求从第k个人开始报数，报到第m个人的时候退出，
#   然后从下一个人开始继续报数并按照同样规则退出，直到所有人退出，
#   要求按顺序输出各出列人数的编号
# 下面首先使用顺序表来实现

# 算法梗概：
# 初始：
#   建立一个包含n个人（的编号）的表
#   找到第k个人，从那里开始
# 处理过程中采用把相应表元素修改为0的方式表示已出列，反复做
#   数m个人（尚在坐），遇到表的末端就转回下标0继续
#   把第m个人的表元素修改为0
# n个人出列即结束

# 下面算法中用n表示总人数，k表示初始第k个人开始报数，
# m表示报到第m个人时退出

def joesphus_list(n, k, m):
    people = list(range(1,n+1))

    i = k-1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i],end='')
                people[i] = 0
            i = (i+1) % n
        if num < n - 1:
            print(', ', end='')
        else:
            print()

    print()
    return

if __name__ == '__main__':
    n = 5
    k = 3
    m = 7
    joesphus_list(n, k, m)



    