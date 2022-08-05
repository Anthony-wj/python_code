import random
lst = list(range(10))
random.shuffle(lst)
def bubble_sort(seq):
    if seq == [] or len(seq) < 2:
        return
    num = len(seq)
    for i in range(num-1):
        for j in range(num-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]

bubble_sort(lst)
print("冒泡排序：", lst)

def select_sort(seq):
    if seq == [] or len(seq) < 2:
        return
    n = len(seq)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if min_idx != i:
            seq[min_idx], seq[i] = seq[i], seq[min_idx]
random.shuffle(lst)
select_sort(lst)
print("选择排序：", lst)

def insert_sort(seq):
    if seq == [] or len(seq) < 2:
        return
    n = len(seq)
    for i in range(1, n):
        pos = i
        while seq[pos] < seq[pos-1] and pos > 0:
            seq[pos-1], seq[pos] = seq[pos], seq[pos-1]
            pos -= 1

random.shuffle(lst)
insert_sort(lst)
print("插入排序：", lst)

def quick_sort1(seq):
    if seq == [] or len(seq) < 2:
        return seq
    pivot_index = 0
    pivot = seq[pivot_index]
    less_part = [i for i in seq[1:] if i <= pivot]
    great_part = [i for i in seq[1:] if i > pivot]
    return quick_sort1(less_part) + [pivot] + quick_sort1(great_part)

random.shuffle(lst)
result1 = quick_sort1(lst)
print("快速排序：", result1)

def partition(seq, beg, end):
    pivot_index = beg
    pivot = seq[pivot_index]
    left = beg+1
    right = end-1
    while True:
        while left <= right and seq[left] <= pivot:
            left += 1
        while left <= right and seq[right] > pivot:
            right -= 1
        if left > right:
            break
        seq[left], seq[right] = seq[right], seq[left]


    seq[pivot_index], seq[right] = seq[right], seq[pivot_index]
    return right


def quick_sort2(seq, beg, end):
    if beg < end:
        pivot = partition(seq, beg, end)
        quick_sort2(seq, beg, pivot)
        quick_sort2(seq, pivot+1, end)

quick_sort2(lst, 0, len(lst))
print("快速排序2.0：", lst)

def merge_sort(seq):
    if seq == [] or len(seq) < 2:
        return seq
    mid = int(len(seq) / 2)
    left_part = merge_sort(seq[:mid])
    right_part = merge_sort(seq[mid:])
    new_list = merge_sorted(left_part, right_part)
    return new_list

def merge_sorted(sorted_a, sorted_b):
    a_length, b_length = len(sorted_a), len(sorted_b)
    a = b = 0
    new_list = []
    while a < a_length and b < b_length:
        if sorted_a[a] <= sorted_b[b]:
            new_list.append(sorted_a[a])
            a += 1
        else:
            new_list.append(sorted_b[b])
            b += 1
    while a < a_length:
        new_list.append(sorted_a[a])
        a += 1
    while b < b_length:
        new_list.append(sorted_b[b])
        b += 1
    return new_list

random.shuffle(lst)
result = merge_sort(lst)
print("归并排序：", result)

def heapify(seq, index,heapSize):
    left = index*2+1
    while left < heapSize:
        largest = left+1 if left+1 < heapSize and seq[left+1] > seq[left] else left
        largest = largest if seq[largest] > seq[index] else index
        if largest == index:
            break
        seq[largest], seq[index] = seq[index], seq[largest]
        index = largest
        left = 2*index+1

def heapinsert(seq, index):
    while seq[index] > seq[int((index-1)/2)]:# 如果父亲比当前节点大，或者当前节点已经到顶了
        seq[index], seq[int((index-1)/2)] = seq[int((index-1)/2)], seq[index]
        index = int((index-1)/2)

def heap_sort(seq):
    if seq == [] or len(seq) < 2:
        return seq
    for i in range(len(seq)):
        heapinsert(seq, i)
    heapSize = len(seq)
    heapSize -= 1
    seq[0], seq[heapSize] = seq[heapSize], seq[0]
    while heapSize > 0:
        heapify(seq, 0, heapSize)
        heapSize -= 1
        seq[0], seq[heapSize] = seq[heapSize], seq[0]
random.shuffle(lst)
heap_sort(lst)
print(lst)
lst.reverse()

