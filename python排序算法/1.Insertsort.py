def Insert_sort(seq):
    if seq == [] or len(seq) < 2:
        return
    for i in range(1, len(seq)):
        pos = i
        while pos>0 and seq[pos-1] > seq[pos]:
            seq[pos], seq[pos-1] = seq[pos-1], seq[pos]
            pos -= 1

lst = list(range(10))
import random
random.shuffle(lst)
Insert_sort(lst)
print(lst)