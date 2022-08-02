class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
# 利用递归行为三次可以到达自己，选择打印的时机不同，可以实现三种遍历
# 先序遍历
def preOrderRecur(head):
    if head == None:
        return
    print(head.value)
    preOrderRecur(head.left)
    preOrderRecur(head.right)

# 中序遍历
def inOrderRecur(head):
    if head == None:
        return
    preOrderRecur(head.left)
    print(head.value)
    preOrderRecur(head.right)

def posOrderRecur(head):
    if head == None:
        return
    preOrderRecur(head.left)
    preOrderRecur(head.right)
    print(head.value)

'''
              5
        3           8
    2      4     7       10
1              6       9       11
'''
if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)

    preOrderRecur(head)
    print("----------------------")
    inOrderRecur(head)
    print("----------------------")
    posOrderRecur(head)

