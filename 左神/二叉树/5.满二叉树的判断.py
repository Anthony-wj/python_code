'''
    最大深度l
    节点数N
    满足 N == 2 ** L -1的树
'''
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def isf(head):
    if not head:
        return True
    height, nodes = process(head)
    return nodes == (2 ** height) -1

def process(head):
    if not head:
        return 0,0
    leftData = process(head.left)
    rightData = process(head.right)
    height = max(leftData[0], rightData[0]) + 1
    nodes = leftData[1] + rightData[1] + 1
    return height, nodes


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    result = isf(head)
    print(result)