# def bubble_sort(seq):
#     if seq == [] or len(seq) < 2:
#         return
#     for i in range(len(seq)-1):
#         for j in range(len(seq)-i-1):
#             if seq[j] > seq[j+1]:
#                 seq[j], seq[j+1] = seq[j+1], seq[j]
#
import random
lst = list(range(10))
random.shuffle(lst)
# bubble_sort(lst)
# print(lst)
#
# def select_sort(seq):
#     if seq == [] or len(seq) < 2:
#         return
#     for i in range(len(seq) - 1):
#         min_idx = i
#         for j in range(i+1, len(seq)):
#             if seq[j] < seq[min_idx]:
#                 min_idx = j
#         if min_idx != i:
#             seq[i], seq[min_idx] = seq[min_idx], seq[i]
# random.shuffle(lst)
# select_sort(lst)
# print(lst)
#
# def insert_sort(seq):
#     if seq == [] or len(seq) < 2:
#         return
#     for i in range(1, len(seq)):
#         pos = i
#         while pos > 0 and seq[pos] < seq[pos-1]:
#             seq[pos], seq[pos-1] = seq[pos-1], seq[pos]
#             pos -= 1
# random.shuffle(lst)
# insert_sort(lst)
# print(lst)
#
# def merge_sort(seq):
#     if seq == [] or len(seq) < 2:
#         return seq
#     mid = int(len(seq) >> 1)
#     left_sorted_list = merge_sort(seq[:mid])
#     right_sorted_list = merge_sort(seq[mid:])
#     new_list = merge_sorted(left_sorted_list, right_sorted_list)
#     return new_list
#
# def merge_sorted(sorted_a, sorted_b):
#     length_a, length_b = len(sorted_a), len(sorted_b)
#     a = b = 0
#     new_sorted_list = list()
#     while a < length_a and b < length_b:
#         if sorted_a[a] <= sorted_b[b]:
#             new_sorted_list.append(sorted_a[a])
#             a += 1
#         else:
#             new_sorted_list.append(sorted_b[b])
#             b += 1
#     while a < length_a:
#         new_sorted_list.append(sorted_a[a])
#         a += 1
#     while b < length_b:
#         new_sorted_list.append(sorted_b[b])
#         b += 1
#     return new_sorted_list
# random.shuffle(lst)
# print(lst)
# new_lst = merge_sort(lst)
# print(new_lst)

def quick_sort(seq, beg, end):
    if beg < end:
        pivot = partition(seq, beg, end)
        quick_sort(seq, beg, pivot)
        quick_sort(seq, pivot+1, end)

def partition(seq, beg, end):
    pivot_index = beg
    pivot = seq[pivot_index]
    left = pivot_index + 1
    right = end - 1
    while True:
        while left <= right and seq[left] < pivot:
            left += 1
        while left <= right and seq[right] >= pivot:
            right -= 1
        if left > right:
            break
        seq[left], seq[right] = seq[right], seq[left]
    seq[pivot_index], seq[right] = seq[right], seq[pivot_index]
    return right
print(lst)
quick_sort(lst, 0, len(lst))
print(lst)