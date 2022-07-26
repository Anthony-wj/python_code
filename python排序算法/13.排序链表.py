# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sortFunc(head):
            if not head or head.next == None:
                return head
            mid = getMid(head)
            l = head 
            r = mid.next
            mid.next = None
            return merge(sortFunc(l), sortFunc(r))

        def getMid(head):
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(head1, head2):
            root = ListNode()
            tmp, tmp1, tmp2 = root, head1, head2
            while tmp1 and tmp2:
                if tmp1.val <= tmp2.val:
                    tmp.next = tmp1
                    tmp1 = tmp1.next
                else:
                    tmp.next = tmp2
                    tmp2 = tmp2.next
                tmp = tmp.next
            if tmp1:
                tmp.next = tmp1
            elif tmp2:
                tmp.next = tmp2
            return root.next
        return sortFunc(head)