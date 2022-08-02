'''
    Q:给定两个可能有环也可能无环的单链表，头结点head1和head2.请实现一个函数吐过两个链表香蕉，请返回香蕉的第一个接点，如果不想交，请返回None
    A:先判断两个链表是否有环
        如果都没有环：再判断两个链表尾结点是否一致，不一致则返回None。
                    一致
        一个有环，另一个没环：不可能会相交，返回None
        两个链表都有环：
            不相交                  loop1转一圈，没有遇到loop2
            入环节点相同             两个入环节点相同
            乳环节点不同，但共用环     loop2转一圈，遇到了loop2

'''
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

#找到链表第一个入环节点，如果无环，返回None
def getLoopNode(head):
    if not head or not head.next or not head.next.next:
        return None
    n1 = head.next
    n2 = head.next.next
    while n1 != n2:
        if n2.next == None or n2.next.next == None:
            return None
        n2 = n2.next.next
        n1 = n1.next
    n2 = head
    while n2 != n1:
        n2 = n2.next
        n1 = n1.next
    return n2


# 如果两个链表都无环，返回第一个相交节点，如果不相交，返回None
def noLoop(head1, head2):
    if head1 == None or head2 == None:
        return None
    cur1 = head1
    cur2 = head2
    n = 0
    while cur1.next:
        n += 1
        cur1 = cur1.next
    while cur2.next:
        n -= 1
        cur2 = cur2.next
    if cur1 != cur2:
        return None
    cur1 = head1 if n > 0 else head2
    cur2 = head2 if cur1 == head1 else head1
    n = abs(n)
    while n != 0:
        n -= 1
        cur1 = cur1.next
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1


# 两个有环链表，返回第一个相交节点，如果不相交，返回None
def bothLoop(head1:  Node, loop1:  Node, head2:  Node, loop2:  Node):
    if loop1 == loop2:
        cur1 = head1
        cur2 = head2
        n = 0
        while cur1 != loop1:
            n += 1
            cur1 = cur1.next
        while cur2 != loop2:
            n -= 1
            cur2 = cur2.next
        cur1 = head1 if n > 0 else head2
        cur2 = head2 if cur1 == head1 else head1
        n = abs(n)
        while n != 0:
            n -= 1
            cur1 = cur1.next
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:
                return loop1
            cur1 = cur1.next
        return None

def getIntersectNode(head1, head2):
    if not head1 or not head2:
        return None
    loop1 = getLoopNode(head1)
    loop2 = getLoopNode(head2)
    if loop1 == None and loop2 == None:
        return noLoop(head1, head2)
    if loop1 != None and loop2 != None:
        return bothLoop(head1, loop1, head2, loop2)
    return None