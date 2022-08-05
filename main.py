import random
lst = list(range(10))
random.shuffle(lst)

def heapInsert(seq, index):
    while seq[index] > seq[int((index-1)/2)]:
        seq[index], seq[int((index-1)/2)] = seq[int((index-1)/2)], seq[index]
        index = int((index-1)/2)

# def heapInsert(seq, index):
#     while seq[index] > seq[int((index-1)/2)]:# 如果父亲比当前节点大，或者当前节点已经到顶了
#         seq[index], seq[int((index-1)/2)] = seq[int((index-1)/2)], seq[index]
#         index = int((index-1)/2)

def heapify(seq, index, heapSize):
    left = 2 * index + 1
    while left < heapSize:
        largest = left+1 if left+1 < heapSize and seq[left+1] > seq[left] else left
        largest = largest if seq[largest] > seq[index] else index
        if largest == index:
            break
        seq[largest], seq[index] = seq[index], seq[largest]
        index = largest
        left = 2 * index + 1

def heap_sort(seq):
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

heap_sort(lst)
print(lst)
print(type(float('inf')))
print(float('-inf'))
m = float('-inf')
a = -10000
print(m < a)