'''
    平衡二叉树：除最下面一层的节点都是满的，且最下面一层的所有节点几种在最左边
    如何判断：
        1.任意节点，有右孩子无左孩子->False
        2.在不违规条件1的情况下，如果遇到了第一个左右孩子不全，则后续所有节点都是叶节点
'''
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def isCompleteTree(root) -> bool:
    if not root:
        return None
    queue = []
    queue.append(root)
    flag = False
    while queue != []:
        curr = queue.pop(0)
        if curr.right and not curr.left: # 条件1
            return False

        if flag and (curr.left != None or curr.right != None): # 条件2
            return False

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

        if not curr.left or not curr.right:# 触发条件2
            flag = True
    return True

if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    result = isCompleteTree(head)
    print(result)
