class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

'''
    准备一张哈希表，存储孩子和父节点的对应关系
'''

def lowestCommonAncester(head, q1, q2):
    if not head:
        return
    hashMap = {}
    lst = []
    process(head, hashMap)
    hashMap[head] = head
    curr = q1
    while curr != hashMap[curr]:
        lst.append(curr)
        curr = hashMap[curr]
    lst.append(head)
    curr = q2
    while curr != head:
        if curr in lst:
            return curr.val
        curr = hashMap[curr]
    return head.val



def process(head, hashMap):
    if not head:
        return
    hashMap[head.left] = head
    hashMap[head.right] = head
    process(head.left, hashMap)
    process(head.right, hashMap)

if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    result = lowestCommonAncester(head, head.left, head.right)
    print(result)