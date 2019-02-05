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
        return str(self.InorderTraversal(self))

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
    
    def GetLeaves(self, root):
        result = []
        
        if root:

            # if node doesn't have left or right then it is a leaf, append it to result
            if root.left is None and root.right is None:
                result.append(root.data)
            
            # if node has left node, traverse left recursively until we hit a leaf
            if root.left:
                result += self.GetLeaves(root.left)
            
            # if node has right node, traverse right recursively until we hit a leaf
            if root.left:
                result += self.GetLeaves(root.right)
        
        # return result
        return result

    # inorder traversal
    # left -> root -> right
    def InorderTraversal(self, root):
        result = []

        if root:
            result = self.InorderTraversal(root.left)
            result.append(root.data)
            result += self.InorderTraversal(root.right)

        return result

# test printing tree leaves
root = Node(1)
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.right.left = Node(5) 
root.right.right = Node(8) 
root.right.left.left = Node(6) 
root.right.left.right = Node(7) 
root.right.right.left = Node(9) 
root.right.right.right = Node(10) 
leaves = root.GetLeaves(root)
print("Nodes: ", root)
print("Number of Leaves: ", len(leaves))
print("Leaves: ", str(leaves))