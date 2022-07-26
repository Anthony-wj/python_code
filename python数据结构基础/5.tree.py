class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        node = Node(value)
        # 如果是棵空树，则直接赋给root节点
        if not self.root or self.root.value is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while True:
                currend_node = queue.pop(0)
                if currend_node.value is None:
                    continue
                if not currend_node.left:
                    currend_node.left = node
                    return
                elif not currend_node.right:
                    currend_node.right = node
                    return
                else:
                    queue.append(currend_node.left)
                    queue.append(currend_node.right)

t = Tree()
for i in range(10):
    t.add(i)