class Node:
    '''Node is a node for implementing a binary tree'''
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = None
        if isinstance(data, list) and len(data) > 0:
            self.data = data.pop(0)
            for item in data:
                self.AddNode(item)
        else:
            self.data = data
    
    def __str__(self):
        return str(self.data)
    
    def __add__(self, other):
        return str(self.data) + other
    
    def __radd__(self, other):
        return other + str(self.data)
    
    def Print(self):
        '''Print prints string representation of binary tree'''
        if self.left:
            self.left.Print()
        print(self.data)
        if self.right:
            self.right.Print()

    def AddNode(self, data):
        '''AddNode adds an element to the binary search tree'''
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.AddNode(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.AddNode(data)
        else:
            self.data = data

    def Find(self, val):
        '''Find finds an element in the binary search tree and returns the node or returns None if not found'''
        if self.data == val:
            return self
        if val < self.data:
            if self.left is None:
                return None
            return self.left.Find(val)
        else:
            if self.right is None:
                return None
            return self.right.Find(val)


# test binary search tree
root = Node([10,13,1,12,92])
root.AddNode(14)
root.Print()
result1 = root.Find(13)
result2 = root.Find(22)
if result1:
    print(result1 + " found")
else:
    print("13 not found")
if result2:
    print(result2 + " found")
else:
    print("22 not found")
