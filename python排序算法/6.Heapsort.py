def heapInsert(seq, index):
    while seq[index] > seq[int((index-1) / 2)]:# 孩子比父亲大，或者index等于0
        seq[index], seq[int((index-1) / 2)] = seq[int((index-1) / 2)], seq[index]
        index = int((index-1) / 2)

def heapify(seq, index, heapSize):
    left = int(index * 2 + 1)
    while left < heapSize: # 下方还有孩子的时候
        largest = left+1 if (left+1) < heapSize and seq[left+1]> seq[left] else left # 将较大孩子的下标给largest
        largest = largest if seq[largest] > seq[index] else index # 父亲和较大孩子之间，谁的值大，把下标给largest
        if largest == index:
            break
        seq[largest], seq[index] = seq[index], seq[largest]
        index = largest
        left = index * 2 + 1

def heap_Sort(seq):
    if seq == [] or len(seq) < 2:
        return
    for i in range(len(seq)):
        heapInsert(seq, i)
    heapSize = len(seq)
    heapSize -= 1
    seq[0], seq[heapSize] = seq[heapSize], seq[0]
    while heapSize > 0:
        heapify(seq, 0, heapSize)
        heapSize -= 1
        seq[0], seq[heapSize] = seq[heapSize], seq[0]

# 两种操作时间复杂度都是O(lgN)
import random
lst = list(range(100))
random.shuffle(lst)
print(lst)
heap_Sort(lst)
print(lst)
