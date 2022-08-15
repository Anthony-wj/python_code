def heapinsert(seq, index):
    while seq[index] > seq[int((index - 1) / 2)]:
        seq[index], seq[int((index - 1) / 2)] = seq[int((index - 1) / 2)], seq[index]
        index = int((index - 1) / 2)


def heapify(seq, index, heapSize):
    left = 2 * index + 1
    while left < heapSize:
        largest = left + 1 if left + 1 < heapSize and seq[left + 1] > seq[left] else left
        largest = largest if seq[largest] > seq[index] else index
        if largest == index:
            return
        seq[largest], seq[index] = seq[index], seq[largest]
        index = largest
        left = 2 * index + 1


def heapsort(seq):
    for i in range(len(seq)):
        heapinsert(seq, i)
    heapSize = len(seq) - 1
    seq[0], seq[heapSize] = seq[heapSize], seq[0]
    while heapSize > 0:
        heapify(seq, 0, heapSize)
        heapSize -= 1
        seq[0], seq[heapSize] = seq[heapSize], seq[0]


import random

lst = list(range(10))
random.shuffle(lst)
heapsort(lst)
print(lst)


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
    先序遍历：根左右
    将头结点入栈，按根右左的顺序进栈，依次弹出的结果为先序遍历
'''


def preOrderUnRecur(head):
    stack = []
    stack.append(head)
    result = []
    while stack != []:
        curr = stack.pop()
        result.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return result


'''
    中序遍历：左根右
'''


def inOrderUnRecur(head):
    stack = []
    result = []
    while stack != [] or head != None:
        if head != None:
            stack.append(head)
            head = head.left
        else:
            curr = stack.pop()
            result.append(curr.val)
            head = curr.right
    return result


'''
    后序遍历：左右根
    将头结点入栈，弹出，按根左右的顺序入栈，依次弹出，将结果保存另一个栈中，依次弹出即为后序遍历

'''


def posOrderUnRecur(head):
    stack1 = []
    result = []
    stack1.append(head)
    while stack1 != []:
        curr = stack1.pop()
        result.append(curr.val)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    result.reverse()
    return result


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    result = preOrderUnRecur(head)
    print(result)
    result = posOrderUnRecur(head)
    print(result)
    result = inOrderUnRecur(head)
    print(result)
