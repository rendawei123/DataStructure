"""
排序算法
"""
import random

"""
二分检索
二分检索只对已经排好序的序列有用
每次找中点然后，判断目标值在中点前面还是终点后面，然后根据范围取值,下一次继续缩小范围
"""

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
- 归并排序
- 希尔排序
- 计数排序

"""

"""
递归快排
递归快排就是首先取一个元素，通过循环找到他的准确位置，然后这个位置不变，并且这个数将列表分为两部分，这两部分通过递归的方式执行上一步操作，直到全部排完序

快速排序是一道典型的运用分治思想的题目
"""
def get_middle(elems, left, right):
    tmp = elems[left]

    while left < right:

        while left < right and elems[right] >= tmp:
            right -= 1
        elems[left] = elems[right]

        while left < right and elems[left] <= tmp:
            left += 1
        elems[right] = elems[left]

    elems[left] = tmp

    return left

def quick_sort(elems, left, right):
    if left < right:
        mid = get_middle(elems, left, right)
        quick_sort(elems, left, mid-1)
        quick_sort(elems, mid+1, right)

"""
堆排序
"""
# 定义向下筛选
def sift_down(elems, e, begin, end):
    i, j = begin, begin*2+1

    while j < end:
        if j + 1 < end and elems[j] > elems[j+1]:
            j += 1
        if e < elems[j]:
            break
        elems[i] = elems[j]
        i, j = j, j*2+1
    elems[i] = e

# 堆排序
def heap_sort(elems):
    end = len(elems)

    # 循环建堆
    for i in range(end//2, -1, -1):
        sift_down(elems, elems[i], i, end)

    # 循环将第一个元素取出，添加到末尾
    for i in range(end-1, 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        sift_down(elems, e, 0, i)



if __name__ == '__main__':
    l = list(range(10))
    # print(l)
    # result = bisection_search(l, 3)
    # print(result)
    random.shuffle(l)
    print(l)
    # bubble_sort(l)
    # choose_sort(l)
    # insert_sort(l)
    # heap_sort(l)
    quick_sort(l, 0, len(l)-1)
    print(l)
