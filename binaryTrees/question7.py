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
    
    def __radd(self, other):
        return other + self.__str__()

    def AddNode(self,data):
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
    
    # postorder traversal without recursion
    # left -> right -> root
    def PostorderTraversal(self, root):
        result = []
        nodeStack = []
        curNode = root

        while 1:

            # traverse tree to the left, appending rightNode and rootNode to stack each iteration
            while curNode:

                # push curNode's right child then curNode to stack
                if curNode.right is not None:
                    nodeStack.append(curNode.right)
                nodeStack.append(curNode)

                # set curNode to left child
                curNode = curNode.left
            
            # set last item from stack to curNode
            curNode = nodeStack.pop()

            # always process right child before root, we must check if last item on stack is equal to curNode.right
            if curNode.right is not None and len(nodeStack) > 0 and curNode.right == nodeStack[-1]:
                nodeStack.pop() # remove right child
                nodeStack.append(curNode) # append root
                curNode = curNode.right
            else:
                result.append(curNode.data)
                curNode = None
            
            if len(nodeStack) == 0:
                break
        
        # return result
        return result

# test printing tree nodes postorder without recursion
arr = [12,1,3,77,23,23,55,23,19,12]
root = Node([i for i in arr])
print("Nodes: ", arr)
print("Postorder Traversal: ", root)