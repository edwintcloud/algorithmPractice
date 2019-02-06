class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self, items=None, head=None):
        self.head = head
        
        if items is not None:
            for item in items:
                self.AddNode(item)

    def __str__(self):
        result = []
        node = self.head
        while node:
            result.append(str(node.data))
            node = node.next
        return " -> ".join(result)

    def __radd__(self, other):
        return other + self.__str__()

    def AddNode(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # we will reverse the list by putting all the nodes into a stack
    # then go through the stack backwards, reversing the pointer on each iteration
    def Reverse(self):
        stack = []
        node = self.head
        while node:
            stack.append(node)
            node = node.next

        # set the head to the last node in stack
        self.head = stack[-1]

        # set the first node in stack to point to None
        stack[0].next = None

        # go through stack backwards, setting next pointer to node at i-1
        for i in range(len(stack)-1, 0, -1):
            stack[i].next = stack[i-1]

    def Reverse_Recursive(self, stack=None):
        
        # build node stack
        if stack is None:
            stack = []
            node = self.head
            while node:
                stack.append(node)
                node = node.next

            # set the head to the last node in stack
            self.head = stack[-1]

            # set the first node in stack to point to None
            stack[0].next = None
        
        # set last node in stack to point to next to last node
        stack[-1].next = stack[-2]

        # recursively run the line above, removing each element as we 
        # go down the stack, once our stack is down to the last node, recursion stops
        if len(stack) > 2:
            self.Reverse_Recursive(stack[:-1])
        

# test linked list
linked_list = LinkedList([5,4,3,3,2,1])
print("Linked List: ", linked_list)
print("Prepare for Reversal!")
linked_list.Reverse()
print("Linked List: ", linked_list)
print("Reverse Reverse!")
linked_list.Reverse_Recursive()
print("Linked List: ", linked_list)
