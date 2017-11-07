"""
排序算法
"""
import random

# 二分检索
def bisection_search(l, val):
    left = 0
    right = len(l)-1
    while left <= right:
        mid = (left + right)//2
        if l[mid] < val:
            left = mid + 1
        elif l[mid] > val:
            right = mid -1

        else:
            return mid

    return None
"""
冒泡排序
每次循环一遍，第拿第i个元素和第i+1个元素比较，如果第i个元素大，则将第i个元素和第i+1个元素互换，这样最后一个就是最大的元素了，然后进行下一次循环，知道所有的都排好序
"""
# 冒泡排序
def bubble_sort(l):
    i = len(l) - 1
    while i > 0:
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
        i -= 1
    return l

"""
选择排序，
每一趟从元素列表中取出最小的元素作为第i个元素
"""
def choose_sort(l):
    end = len(l)
    for i in range(end):
        min = i

        for j in range(i,end):
            if l[j] < l[min]:
                min = j

        l[i], l[min] = l[min], l[i]
    return l

"""
插入排序
列表被分为有序区和无序区两个部分。最初有序区只有一个元素。
每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空。
"""
def insert_sort(l):
    for i in range(1, len(l)):
        tmp = l[i]
        j = i - 1
        while j >= 0 and l[j] > tmp:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = tmp
    return l

"""
检索

- 二分查找

排序

- 冒泡排序
- 选择排序
- 插入排序
- 递归快拍
- 堆排序
- 归并排序
- 希尔排序
- 计数排序

"""


if __name__ == '__main__':
    l = list(range(10))
    # print(l)
    # result = bisection_search(l, 3)
    # print(result)
    random.shuffle(l)
    print(l)
    # bubble_sort(l)
    # choose_sort(l)
    insert_sort(l)
    print(l)
