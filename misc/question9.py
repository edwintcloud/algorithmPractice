class Stack:

    def __init__(self, data=[]):
        self.data = []
        self.min = 0
        self.max = 0
        self.sorted = []
        if len(data) > 0:
            self.min = data[0]
            for item in data:
                if item > self.max:
                    self.max = item
                if item < self.min:
                    self.min = item
                self.data.append(item)
            self.sorted = sorted(self.data)
    
    def __str__(self):
        return str(self.data)
    
    def __radd__(self, other):
        return other + self.__str__()

    def pop(self):
        item = self.data.pop()
        if item == self.max:
            self.max = self.sorted[-1]
            self.sorted.pop()
        if item == self.min:
            self.min = self.sorted[0]
            self.sorted.pop(0)
        return item
    
    def push(self, data):
        if data > self.max:
            self.max = data
        if data < self.min:
            self.min = data
        self.data.append(data)

    def min(self):
        return self.min
    
    def max(self):
        return self.max

# test stack
arr = [3,55,32,12,4,16,55,9,92,13,44,13]
print("Stack: ", arr)
result = Stack(arr)
print("Min: ", result.min, "Max: ", result.max)
result.push(101)
print("Adding 101 to the stack")
print("Stack: ", result)
print("Min: ", result.min, "Max: ", result.max)
result.push(1)
print("Adding 1 to the stack")
print("Stack: ", result)
print("Min: ", result.min, "Max: ", result.max)
result.pop()
print("Popping the stack")
print("Stack: ", result)
print("Min: ", result.min, "Max: ", result.max)
result.pop()
print("Popping the stack")
print("Stack: ", result)
print("Min: ", result.min, "Max: ", result.max)
result.pop()

