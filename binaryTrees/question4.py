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

    # inorder traversal
    # left -> root -> right
    def InorderTraversal(self, root):
        result = []
        if root:
            result = self.InorderTraversal(root.left)
            result.append(root.data)
            result += self.InorderTraversal(root.right)
        return result
    
# test inorder traversal
arr = [12,1,3,77,23,23,55,23,19,12]
root = Node([i for i in arr])
print("Nodes: ", arr)
print("Inorder Traversal: ", root.InorderTraversal(root))