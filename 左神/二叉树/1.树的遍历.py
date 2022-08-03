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

def preOrderUnRecur(head):
    '''
    1.先将头结点入栈，弹出
    2.处理这个节点
    3.再将右孩子入栈、左孩子入栈，如果有的话
    4.循环直至栈空
    :param head:
    :return:
    '''
    if not head:
        return
    stack = []
    stack.append(head)
    pre_list = []
    while stack != []:
        head = stack.pop()
        pre_list.append(head.value)
        if head.right != None:
            stack.append(head.right)
        if head.left != None:
            stack.append(head.left)
    return pre_list


# 中序遍历
def inOrderRecur(head):
    if head == None:
        return
    inOrderRecur(head.left)
    print(head.value)
    inOrderRecur(head.right)

def inOrderUnRecur(head):
    '''
    每棵子树，整棵树的左边界进栈，依次弹出的过程中打印，对弹出节点的右树循环以上步骤
    :param head:
    :return:
    '''
    if not head:
        return
    stack = []
    in_list = []
    while stack != [] or head != None:
        if head != None:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            in_list.append(head.value)
            head = head.right
    return in_list
'''
              1
        2           3
    4      5     6      7
'''

def posOrderRecur(head):
    if head == None:
        return
    posOrderRecur(head.left)
    posOrderRecur(head.right)
    print(head.value)

def posOrderUnRecur(head):
    '''
    将头结点入栈
    1.弹出当前节点curr
    2，curr入收集栈
    3.先左再右依次入栈
    4.循环直至栈空
    5.依次弹出收集栈，即为后序遍历
    根左右入栈，出栈为根右左，进入收集栈中出栈顺序为左右根
    :param head:
    :return:
    '''
    if not head:
        return
    stack1 = []
    stack2 = []
    stack1.append(head)
    while stack1 != []:
        head = stack1.pop()
        stack2.append(head.value)
        if head.left != None:
            stack1.append(head.left)
        if head.right != None:
            stack1.append(head.right)
    stack2.reverse()
    return stack2
'''
              1
        2           3
    4      5     6      7
    先序遍历: 1 2 4 5 3 6 7
    中序遍历：4 2 5 1 6 3 7
    后序遍历：4 5 2 6 7 3 1
'''
if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)

    # preOrderRecur(head)
    # print("----------------------")
    # inOrderRecur(head)
    # print("----------------------")
    # posOrderRecur(head)
    # print("----------------------")
    pre_list = preOrderUnRecur(head)
    print(pre_list)
    pos_list = posOrderUnRecur(head)
    print(pos_list)
    in_list = inOrderUnRecur(head)
    print(in_list)
