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

    def __str__(self):
        return str(self.PostorderTraversal(self))
    
    def __radd__(self, other):
        return other + self.__str__()

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

    # postorder traversal
    # left -> right -> root
    def PostorderTraversal(self, root):
        result = []
        if root:
            result = self.PostorderTraversal(root.left)
            result += self.PostorderTraversal(root.right)
            result.append(root.data)
        return result

# test printing tree nodes postorder
arr = [12,1,3,77,23,23,55,23,19,12]
root = Node([i for i in arr])
print("Nodes: ", arr)
print("Postorder Traversal: ", root)