class queue:
    def __init__(self, maxsize = None):
        self.list = []

    def in_queue(self, value):
        self.list.append(value)

    def out_queue(self):
        self.list.pop(0)

    def print_queue(self):
        print(self.list)

    def __len__(self):
        return len(self.list)

q = queue()
q.in_queue(1)
q.in_queue(2)
print(len(q))
q.out_queue()
q.print_queue()