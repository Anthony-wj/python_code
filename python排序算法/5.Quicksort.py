# def quick_sort1(seq):
#     if seq == [] or len(seq) < 2:
#         return seq
#     pivot_index = 0
#     pivot = seq[pivot_index]
#     less_part = [i for i in seq[pivot_index+1:] if i <= pivot]
#     great_part = [i for i in seq[pivot_index+1:] if i > pivot]
#     return quick_sort1(less_part) + [pivot] + quick_sort1(great_part)
#
# import random
# lst = list(range(10))
# random.shuffle(lst)
# lst = quick_sort1(lst)
# print(lst)
#
# def quick_sort2(seq, beg, end):
#     if beg < end:
#         pivot = partition(seq, beg, end)
#         quick_sort2(seq, beg, pivot)
#         quick_sort2(seq, pivot+1, end)
#
# def partition(seq, beg, end):
#     pivot_index = beg
#     pivot = seq[pivot_index]
#     left = pivot_index + 1
#     right = end - 1
#     while True:
#         while left <= right and seq[left] < pivot:
#             left += 1
#         while left <= right and seq[right] > pivot:
#             right -= 1
#         if left > right:
#             break
#         seq[left], seq[right] = seq[right], seq[left]
#     seq[pivot_index], seq[right] = seq[right], seq[pivot_index]
#     return right
# random.shuffle(lst)
# quick_sort2(lst, 0, len(lst))
# print(lst)

def quick_sort1(seq):
    if seq == [] or len(seq)<2:
        return seq
    else:
        pivot_index = 0
        pivot = seq[pivot_index]
        less_part = [i for i in seq[pivot_index+1:] if i <= pivot]
        great_part = [i for i in seq[pivot_index+1:] if i >pivot]
        return quick_sort1(less_part) + [pivot] + quick_sort1(great_part)

import random
lst = list(range(10))
random.shuffle(lst)
lst = quick_sort1(lst)
print(lst)