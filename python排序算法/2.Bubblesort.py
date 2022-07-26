# 每轮循环将最大的数沉到海底
def bubble_sort(seq):
    if seq == [] or len(seq) < 2:
        return
    for i in range(len(seq)-1):
        for j in range(len(seq)-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]

import random
lst = list(range(10))
random.shuffle(lst)
bubble_sort(lst)
print(lst)