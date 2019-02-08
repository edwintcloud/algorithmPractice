class Stack:
    '''Stack is a class implmentation of a stack'''

    def __init__(self, items=[]):
        self.data = []
        self.maxes = []

        if len(items) > 0:
            for item in items:
                self.push(item)

    def __str__(self):
        return str(self.data)

    def __radd__(self, other):
        return other + self.__str__()

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        item = self.data.pop()
        if item == self.max():
            self.maxes.pop()
        return item

    def push(self, item):
        if len(self.maxes) == 0:
            self.maxes.append(item)
        elif item >= self.max():
            self.maxes.append(item)
        self.data.append(item)

    def peek(self):
        if self.is_empty():
            raise Exception("stack is empty")
        return self.data[-1]

    def is_empty(self):
        return True if len(self.data) == 0 else False

    def max(self):
        return self.maxes[-1]


## TEST ##
stack = Stack()
stack.push(8)
print("Stack:", stack, "Peek:", stack.peek(), "Max:", stack.max())
stack.push(18)
print("Stack:", stack, "Peek:", stack.peek(), "Max:", stack.max())
stack.push(19)
print("Stack:", stack, "Peek:", stack.peek(), "Max:", stack.max())
stack.push(2)
print("Stack:", stack, "Peek:", stack.peek(), "Max:", stack.max())
stack.pop()
print("Stack:", stack, "Peek:", stack.peek(), "Max:", stack.max())
stack.pop()
print("Stack:", stack, "Peek:", stack.peek(), "Max:", stack.max())
stack.pop()
print("Stack:", stack, "Peek:", stack.peek(), "Max:", stack.max())
stack.push(9)
print("Stack:", stack, "Peek:", stack.peek(), "Max:", stack.max())
stack.push(9)
print("Stack:", stack, "Peek:", stack.peek(), "Max:", stack.max())
stack.pop()
print("Stack:", stack, "Peek:", stack.peek(), "Max:", stack.max())
stack.pop()
print("Stack:", stack, "Peek:", stack.peek(), "Max:", stack.max())


