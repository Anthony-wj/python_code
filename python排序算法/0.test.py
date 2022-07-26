def merge_sort(seq):
    if seq == [] or len(seq) < 2:
        return seq
    mid = int(len(seq) >> 1)
    left_sorted = merge_sort(seq[:mid])
    rigth_sorted = merge_sort(seq[mid:])
    new_sorted_list = merge_sorted(left_sorted, rigth_sorted)
    return new_sorted_list

def merge_sorted(sorted_a, sorted_b):
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_list = list()
    while a < length_a and b < length_b:
        if sorted_a[a] <= sorted_b[b]:
            new_list.append(sorted_a[a])
            a += 1
        else:
            new_list.append(sorted_b[b])
            b += 1
    while a < length_a:
        new_list.append(sorted_a[a])
        a += 1
    while b < length_b:
        new_list.append(sorted_b[b])
        b += 1
    return new_list

import random
lst = list(range(10))
random.shuffle(lst)
lst = merge_sort(lst)
print(lst)

def insert_sort(seq):
    if seq == [] or len(seq) < 2:
        return seq
    for i in range(1, len(seq)):
        pos = i
        while pos > 0 and seq[pos-1] > seq[pos]:
            seq[pos-1], seq[pos] = seq[pos], seq[pos-1]
            pos -= 1

random.shuffle(lst)
insert_sort(lst)
print(lst)

def select_sort(seq):
    if seq == [] or len(seq) < 2:
        return seq
    for i in range(len(seq)-1):
        min_idx = i
        for j in range(i, len(seq)):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if min_idx != i:
            seq[min_idx], seq[i] = seq[i], seq[min_idx]

random.shuffle(lst)
select_sort(lst)
print(lst)
