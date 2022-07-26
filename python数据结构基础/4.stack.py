class stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def isempty(self):
        return len(self.list) == 0

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            return self.list.pop()
    def gettop(self):
        if self.isempty():
            print("stack is empty")
        else:
            return self.list[-1]

s = stack()
s.push(1)
s.push(2)
s.pop()
s.pop()
print(s.gettop())