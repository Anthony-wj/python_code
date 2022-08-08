class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

'''
搜索二叉树：任意一个节点，左孩子比它小，右孩子比它大，那这棵树就是搜搜二叉树
    如何判断： 中序遍历，保持升序则为搜索二叉树
'''
# preValue = float('-inf')
def isBST1(head):
    global preValue
    if not head:
        return True
    isLeftBst = isBST1(head.left) # 检查左树是否为搜索二叉树

    if not isLeftBst: # 如果左树不是搜索二叉树，直接返回False
        return False
    if head.value <= preValue: # 如果不是升序，则说明不是搜索二叉树
        return False
    else:
        preValue = head.value # 是升序则依次遍历

    return isBST1(head.right) # 右树不是搜索二叉树，直接返回False。右树是搜索二叉树，因为左树已经确定是搜索二叉树，直接返回True，说明整棵树是搜索二叉树


def process2(head, lst):
    process2(head.left, lst)
    lst.append(head)
    process2(head.right, lst)

def isBST2(root):
    lst = []
    process2(root)
    preValue = lst[0].val
    for head in lst[1:]:
        if head.val <= preValue:
            return False
        else:
            preValue = head.val
    return True

def isBST3(head):
    '''
    每棵子树，整棵树的左边界进栈，依次弹出的过程中打印，对弹出节点的右树循环以上步骤
    :param head:
    :return:
    '''
    if not head:
        return
    preValue = float('-inf')
    stack = []
    in_list = []
    while stack != [] or head != None:
        if head != None:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            # in_list.append(head.value)
            if head.value <= preValue:
                return False
            else:
                preValue = head.value
            head = head.right
    return True

class ReturnType:
    def __init__(self, isBst=None, max=None, min=None):
        self.isBst=isBst
        self.max=max
        self.min=min

def isBSTRecur(head):
    def isBST(head):
        # 如果是空节点，返回None
        if not head:
            return None
        leftData = isBST(head.left)
        rightData = isBST(head.right)
        # 如果左树不为None
        if leftData!= None:
            minn = leftData.min if leftData.min < head.val else head.val
        else:
            minn = head.val
        # 如果右树不为None
        if rightData != None:
            maxx = rightData.max if rightData.max > head.val else head.val
        else:
            maxx = head.val
        # 不出现违规情况，说明当前树是搜索二叉树
        isBst = True
        # 当左树不为空时，如果左树不是搜索二叉树或者左树的最大值大于或等于当前节点，则当前树不是搜索二叉树
        if leftData != None and (leftData.isBst != True or leftData.max >= head.val):
            isBst = False
        # 当右树不为空时，如果右树不是搜索二叉树或者右树的最小值小于或等于当前节点，则当前树不是搜索二叉树
        if rightData != None and (rightData.isBst != True or rightData.min <= head.val):
            isBst = False
        return ReturnType(isBst=isBst, max=maxx, min=minn)

    return isBST(head).isBst
if __name__ == '__main__':
    head = TreeNode(2)
    head.left = TreeNode(1)
    head.right = TreeNode(3)
    result = isBSTRecur(head)
    print(result)
