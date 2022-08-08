'''
    方法1：中序遍历，将遍历的节点放入链表，打印指定节点的下一个节点即可
    方法2：
        1）x有右孩子的时候，后继节点为父
        2）x无右孩子时，则判断父节点的情况，如果父节点是爷节点的左孩子，则返回爷节点；不是的话继续往上找
'''

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def GetSuccessorNode(head):
    if not head:
        return head
    if head.right != None:
        return getLeftMost(head.right)
    else:
        parent = head.parent
        while head != None and parent.left != head:
            node = parent
            parent = node.parent
        return parent

def getLeftMost(head):
    if not head:
        return head
    while head.left != None:
        head = head.left
    return head

if __name__ == '__main__':
    head = TreeNode(2)
    head.left = TreeNode(1)
    head.right = TreeNode(3)
    head.parent = None
    head.left.parent = head
    head.right.parent = head
    result = GetSuccessorNode(head.left)
    print(result.value)