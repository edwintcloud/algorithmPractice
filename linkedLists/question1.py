class Node:
    
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode

    # find middle uses a slow pointer and fast pointer (1 ahead) to find the middle
    # element of a singly linked list
    def find_middle(self):
        slow_pointer = self
        fast_pointer = self
        while fast_pointer.next and fast_pointer.next.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer.data

# test find_middle function
n6 = Node(7)
n5 = Node(6, n6)
n4 = Node(5, n5)
n3 = Node(4, n4)
n2 = Node(3, n3)
n1 = Node(2, n2)
head = Node(1, n1)
middle = head.find_middle()
print("Linked List: ", "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7")
print("Middle Node: ", middle)

