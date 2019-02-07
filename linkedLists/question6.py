class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self, items=None, head=None):
        self.head = head
        self.size = 1

        if items is not None:
            self.size = 0
            for item in items:
                self.AddNode(item)

    def __str__(self):
        result = []
        cur = self.head
        while cur:
            result.append(str(cur.data))
            cur = cur.next
        return " -> ".join(result)
    
    def __radd__(self, other):
        return other + self.__str__()

    def AddNode(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        self.size += 1

# test function
arr = [5,4,3,2,1]
linked_list = LinkedList(arr)
print(linked_list)
print("Size: ", linked_list.size)
linked_list.AddNode(6)
print(linked_list)
print("Size: ", linked_list.size)