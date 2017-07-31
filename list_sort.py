# 下面定义顺序表插入排序法,将顺序表按照i分为两部分，i前面的为排好序的，
# 后面的为未排好序的，然后提取后面的元素，依次和前面的排好序的序列比较
# 然后选择合适的位置插入，直到i到最后一个元素时，排序结束
# 排序总共使用了两次循环
# 由于后面的未排序的没减少一个，前面的排好序的就会增加一个
# 因此，顺序表插入排序法不会占用多余的内存

#
# def list_sort(list1):
#     for i in range(1, len(list1)):
#         d = list1[i]
#         j = i
#         while j > 0:
#             list1[j] = list1[j-1]
#             if d > list1[j]:
#                 list1[j] = d
#                 break
#             else:
#                 j -= 1


def list_sort(list1):
    for i in range(1, len(list1)):
        x = list1[i]
        j = i
        while j > 0 and list1[j-1] > x:
            list1[j] = list1[j-1]
            j -= 1
        list1[j] = x

if __name__ == '__main__':
    l1 = [1, 3, 8, 2, 5, 4, 7]
    list_sort(l1)
    print(l1)