'''
    左树平衡
    右树平衡
    左树右树高度之差不大于1
'''

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class ReturnType:
    def __init__(self, isBalanced = None, height = 0):
        self.isBalanced = isBalanced
        self.height = height

def isBalanced(head):
    return process(head).isBalanced

def process(head):
    if not head:
        return ReturnType(isBalanced=True, height=0)
    leftData = process(head.left)
    rightData = process(head.right)
    height = max(leftData.height, rightData.height) + 1
    isBalanced = leftData.isBalanced and rightData.isBalanced and abs(leftData.height - rightData.height) < 2
    return ReturnType(isBalanced, height)

def isBalanced2(head):
    return process2(head)[1]

def process2(head):
    if not head:
        return True, 0
    leftData = process2(head.left)
    rightData = process2(head.right)
    height = max(leftData[1], rightData[1]) + 1
    isBalanced = leftData[0] and rightData[0] and abs(leftData[1]-rightData[1])<2
    return isBalanced, height


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    result = isBalanced2(head)
    print(result)
