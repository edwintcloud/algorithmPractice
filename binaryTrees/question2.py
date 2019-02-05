class Node:

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

    def AddNode(self, data):
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

    def Print(self):
        if self.left:
            self.left.Print()
        print(self.data)
        if self.right:
            self.right.Print()
        
    def PreorderTraversal(self, rootNode):
        '''Preorder Traversal: Root -> Left -> Right'''
        result = []
        if rootNode:
            result.append(rootNode.data)
            result +=  self.PreorderTraversal(rootNode.left)
            result += self.PreorderTraversal(rootNode.right)
        return result


# Test preorder traversal
arr = [12,1,3,77,23,23,55,23,19,12]
root = Node([i for i in arr])
print("Nodes: ", arr)
print("Preorder Traversal: ", root.PreorderTraversal(root))