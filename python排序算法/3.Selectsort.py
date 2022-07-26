def select_sort(seq):
    if seq == [] or len(seq) < 2:
        return
    for i in range(len(seq)-1):
        min_idx = i
        for j in range(i, len(seq)):
            if seq[j] < seq[min_idx]:
                idx = j
        if idx != i:
            seq[i], seq[min_idx] = seq[min_idx], seq[i]

import random
lst = list(range(10))
random.shuffle(lst)
select_sort(lst)
print(lst)
