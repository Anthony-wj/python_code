class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def serialize(head):
    if not head: # 如果是空节点返回
        return "#_"
    res = str(head.val) + "_"
    res += serialize(head.left) # 拼接
    res += serialize(head.right) # 拼接
    return res

def reconByPreString(prestr):
    queue = prestr.split("_") # 将字符串切割成列表
    return reconPreOrder(queue) # 对列表进行处理生成树

def reconPreOrder(queue):
    value = queue.pop(0) # 弹出节点，判断
    if value == "#": # 为#则返回None
        return None
    head = TreeNode(value) # 生成节点
    head.left = reconPreOrder(queue) # 遍历
    head.right = reconPreOrder(queue) # 遍历
    return head # 返回节点
if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    res = serialize(head)
    head2 = reconByPreString(res)
    print(head2.val)
