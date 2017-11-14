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


"""
归并排序

归并排序采用分组处理，也是二分法的思想。将一组数据拆成两组，再将小组继续拆分为两个直到每个小组剩下1或0个元素。这时才开始对小组中的元素排序，排序完成之后再合并为新的小组。一直往上排序和合并直到排序完成。
"""
# 首先定义将两个列表进行合并和排序
def merge(left, right):
    i = 0  # 定义left的第一个索引
    j = 0  # 定义right的第一个索引
    result = []

    while i < len(left) and j < len(right):
        # 逐个比较两个列表的元素，小的添加进列表，大的留在后面继续比较
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 最后加上末尾的元素
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(elems):
    length = len(elems)

    # 递归退出条件判断
    if length <= 1:
        return elems

    mid = length // 2
    left = merge_sort(elems[:mid])
    right = merge_sort(elems[mid:])

    # 合并排序
    return merge(left, right)


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
    # quick_sort(l, 0, len(l)-1)
    print(merge_sort(l))
    print(l)
