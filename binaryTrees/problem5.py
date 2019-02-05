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

    # inorder traversal
    # left -> root -> right
    def InorderTraversal(self, root):
        result = []
        nodeStack = []

        currentNode = root

        # travel left through tree until we reach left-most node
        # once we reach left-most node, append data and travel to right node in same subtree
        # then head back up the tree, repeating this process for each subtree
        while 1:
            if currentNode is not None:
                nodeStack.append(currentNode)
                currentNode = currentNode.left
            else:
                if len(nodeStack) == 0:
                    break
                currentNode = nodeStack.pop()
                result.append(currentNode.data)
                currentNode = currentNode.right

        # return result
        return result

# test printing tree nodes inorder without recursion
arr = [12,1,3,77,23,23,55,23,19,12]
root = Node([i for i in arr])
print("Nodes: ", arr)
print("Inorder Traversal: ", root)