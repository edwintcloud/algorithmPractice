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

# detect_cycle
# returns tuple of t/f for cycle and start node of cycle
def detect_cycle(head):
    node = head
    visited = set()
    nodeList = []
    while node:
        if node in visited:
            return True, nodeList.pop().data
        visited.add(node)
        nodeList.append(node)
        node = node.next
    return False, None

# test functions
n6 = Node(7)
cycle = Node(3, n6)
n6.next = cycle
n5 = Node(6, n6)
n4 = Node(5, n5)
n3 = Node(4, n4)
n2 = Node(3, n3)
n1 = Node(2, n2)
head = Node(1, n1)
linked_list = LinkedList(None, head)
result = detect_cycle(head)
if result[0]:
    print("Cycle detected at Node: ", result[1])
else:
    print("Linked List: " + linked_list)