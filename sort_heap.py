"""
堆排序

步骤：
    1.循环建堆
    2.输出一个元素，将这个元素添加在末尾空出来的空间，这样，不会占用多于的空间
"""

def sort_heap(elems):
    # 定义向下筛选
    def siftdown(elems, e, begin, end):
        i, j = begin, begin*2 + 1
        while j < end:
            if j + 1 < end and elems[j] > elems[j + 1]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j*2+1

        elems[i] = e

    end = len(elems)
    # 将序列变为堆
    for i in range(end//2, -1, -1):
        siftdown(elems, elems[i], i, end)

    # 循环弹出，添加到末尾
    for i in range((end-1), 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)

if __name__ == '__main__':
    a = [1,3,6,2,4,8]
    sort_heap(a)
    print(a)
