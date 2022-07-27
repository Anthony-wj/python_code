class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    # 增
    def append(self, value): # 在末尾添加
        node = Node(value)
        if self.length == 0:
            self.root.next = node
        else:
            self.tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value): # 在首部添加
        node = Node(value)
        if self.length == 0:
            self.root.next = node
            self.tailnode = node
        head = self.root.next
        self.root.next = node
        node.next = head
        self.length += 1

    def insert(self, index, value):
        if index<0 or index >self.length:
            print("error:out of index")
            return
        if self.isEmpty():
            print("this link is empty")
            return
        node = Node(value)
        if index == 0:
            cur_node = self.root.next
            self.root.next = node
            node.next = cur_node
            self.tailnode = node
            self.length += 1
            return
        count = 1
        cur_node = self.root.next
        while count < index:
            cur_node = cur_node.next
            count += 1
        node.next = cur_node.next
        cur_node.next = node
        self.length += 1

    def iter_node(self):
        cur_node = self.root.next
        while cur_node is not None:
            print(cur_node.value)
            cur_node = cur_node.next
        return
    # 删
    def pop(self, index = None):
        if index == None:
            if self.length == 0:
                print("链表已空")
            elif self.length == 1:
                self.root.next = None
                self.tailnode = None
                self.length -= 1
            else:
                cur_node = self.root.next
                while cur_node.next is not self.tailnode:
                    cur_node = cur_node.next
                cur_node.next = None
                self.tailnode = cur_node
                self.length -= 1
        else:
            pass
    def popleft(self):
        if self.length == 0:
            print("链表已空")
        elif self.length == 1:
            self.root.next = None
            self.tailnode = None
            self.length -= 1
        else:
            self.root.next = self.root.next.next
            self.length -= 1

    def remove(self, value):
        if self.length == 0:
            print("链表已空")
        else:
            curnode = self.root.next
            if curnode.value == value:
                self.root.next == curnode.next
                self.length -= 1
                return
            while curnode.next is not self.tailnode:
                if curnode.next.value == value:
                    curnode.next = curnode.next.next
            self.length -= 1

    # 查
    def find(self, value):
        if self.length == 0:
            print("链表已空")
        else:
            cur_node = self.root.next
            while cur_node is not self.tailnode:
                if cur_node.value == value:
                    print("Exited")
                    return
                cur_node = cur_node.next
            print("Not exited")




def insertionSortList(head):
    if not head:
        return
    if not head.next:
        return head
    curr = head.next
    root = Node()
    root.next = head
    while curr:
        prev = root
        while prev.next.value <= curr.value:
            prev = prev.next
        next = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = next
    return root.next


l = LinkedList()
l.append(1)
l.append(3)
l.append(2)
result = insertionSortList(l.root.next)
print(result.value)