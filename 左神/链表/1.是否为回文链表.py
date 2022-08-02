


'''
    Q:判断链表是否为回文链表？
    A1: 遍历链表将所有节点值入栈。遍历链表，每次出栈的元素和节点对比是否相同，相同则继续遍历，直至栈空，一旦有元素不同则不是回文链表
    A2: 值将链表的右半部分入栈，接下来继续遍历和出栈(需要快慢指针来获取中间节点)
    A3: 将链表的后半部分进行翻转，1 2 3 3 2 1
'''

'''
# Version1  时间复杂度为O(N) 空间复杂度为O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if stack.pop() != curr.val:
                return False
            else:
                curr = curr.next
        return True
'''

'''
# Version2 时间复杂度为O(N) 空间复杂度为O(N/2)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        stack = []
        while slow:
            stack.append(slow.val)
            slow = slow.next
        curr = head
        while stack != []:
            if stack.pop() != curr.val:
                return False
            else:
                curr = curr.next
        return True
'''

'''
# version3  时间复杂度O(N) 空间复杂度为O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid_node = slow
        prev = None
        curr = slow
        while curr:
            next= curr.next
            curr.next = prev
            prev = curr
            curr = next
        last = prev
        curr = head
        while curr and last:
            if curr.val != last.val:
                return False
            else:
                curr = curr.next
                last = last.next
        return True
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
curr = head
for i in range(2, 7):
    node = ListNode(i)
    curr.next = node
    curr = curr.next
curr = head

while curr:
    print(curr.val)
    curr = curr.next

slow = head
fast = head

while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next

print(slow.val)
