'''
    root 指向头结点
    lastSorted 已排序序列的最后一个节点
    curr 待插入元素
    
'''
# 1 3 2 4
'''
    特殊情况：
        如果是个空链表，直接返回
        lastSorted比curr小，则直接让lastSorted=lastSorted.next; curr=lastSorted.next
        curr比头结点小，则需要加一个root节点，root节点指向头结点
    正常情况：
        定义一个prev节点，从头开始遍历
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self):
        self.length = 0
        self.head = ListNode()
        self.tailnode = None


    def append(self, value):
        node = ListNode(value)
        if self.head.val is None:
            self.head = node
        else:
            self.tailnode.next = node
        self.tailnode = node
        self.length += 1

    def iter_node(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.val)
            curr_node = curr_node.next
        return





def insertionSortList(head: ListNode) -> ListNode:
    if not head:
        return head

    root = ListNode()
    root.next = head
    lastSorted = head
    curr = head.next

    while curr:
        if lastSorted.val <= curr.val:
            lastSorted = lastSorted.next
            curr = lastSorted.next
        else:
            prev = root
            while prev.next.val <= curr.val:
                prev = prev.next
            lastSorted.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = lastSorted.next
    return root.next

import random
l = LinkList()
lst = list(range(10))
random.shuffle(lst)
print(lst)
for i in lst:
    l.append(i)
sorted_List = insertionSortList(l.head)