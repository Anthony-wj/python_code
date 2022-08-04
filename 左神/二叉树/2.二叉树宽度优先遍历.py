'''
    宽度优先用队列
    将当前节点入队列
    弹出节点并将左右孩子依次入队列(有的话)

'''
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def w(head):
    if not head:
        return
    queue = []
    queue.append(head)
    lst = []
    while queue != []:
        curr = queue.pop(0)
        lst.append(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return lst

def maxWidth(head):
    if not head:
        return
    queue = []
    levelMap = {}
    queue.append(head)
    levelMap[head] = 1
    curlevel = 1
    curlevelNodes = 0
    max = -1
    while queue != []:
        curr = queue.pop(0)
        curNodeLevel = levelMap.get(curr)

        # 如果当前节点层 和 当前所在层一致，则当前层的节点+1
        if curNodeLevel == curlevel:
            curlevelNodes += 1
        # 不一致时，说明该进入下一层了，curlevel+=1，并且因为直到当前节点属于下一层，锁curlevelNodes=1
        else:
            max = max if max > curlevelNodes else curlevelNodes
            curlevel += 1
            curlevelNodes = 1
        if curr.left:
            queue.append(curr.left)
            levelMap[curr.left] = curNodeLevel+1
        if curr.right:
            queue.append(curr.right)
            levelMap[curr.right] = curNodeLevel+1
    max = max if max > curlevelNodes else curlevelNodes
    return max

def maxWidth2(head):
    # 使用哈希表的情况
    if not head:
        return
    queue = []
    levelMap = {}
    queue.append(head)
    levelMap[head] = 1
    curlevel = 1
    curlevelNodes = 0
    max = -1
    lst = []
    result = []
    while queue != []:
        curr = queue.pop(0)
        curNodeLevel = levelMap.get(curr)

        # 如果当前节点层 和 当前所在层一致，则当前层的节点+1
        if curNodeLevel == curlevel:
            curlevelNodes += 1
            lst.append(curr.value)
        # 不一致时，说明该进入下一层了，curlevel+=1，并且因为直到当前节点属于下一层，锁curlevelNodes=1
        else:
            result.append(lst)
            lst = []
            lst.append(curr.value)
            max = max if max > curlevelNodes else curlevelNodes
            curlevel += 1
            curlevelNodes = 1
        if curr.left:
            queue.append(curr.left)
            levelMap[curr.left] = curNodeLevel+1
        if curr.right:
            queue.append(curr.right)
            levelMap[curr.right] = curNodeLevel+1
    max = max if max > curlevelNodes else curlevelNodes
    result.append(lst)
    return result

def maxwidth3(head):
    # 不使用哈希表的情况
    if not head:
        return
    queue = []
    queue.append(head)
    # 定义当前节点所在层的末尾节点cur_end
    cur_end = head
    # 定义当前节点所在层的下一层的末尾节点next_end
    next_end = None
    # 定义当前层的节点数
    curNodes = 0
    max = -1
    result = []
    lst = []
    while queue != []:
        # 先弹出队列的元素，让当前节点数+1
        curr = queue.pop(0)
        lst.append(curr.value)
        curNodes += 1
        # 再让当前节点的左孩子进队列，next_end设置为左孩子;然后让右孩子进队列，next_end设置为右孩子。(前提是孩子存在)
        if curr.left:
            queue.append(curr.left)
            next_end = curr.left
        if curr.right:
            queue.append(curr.right)
            next_end = curr.right
        # 判断当前节点是否为所在层的尾节点，如果是，则统计当前层的节点数，进入下一层。
        if curr == cur_end:
            result.append(lst)
            lst = []
            max = max if max > curNodes else curNodes
            curNodes = 0
            cur_end = next_end
            next_end = None
    return result


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)

    lst = w(head)
    print(lst)
    max = maxwidth3(head)
    print(max)