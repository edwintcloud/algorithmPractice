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
        root = self.head
        while root:
            result.append(str(root.data))
            root = root.next
        return " -> ".join(result)

    def __radd__(self, other):
        return other + self.__str__()

    def AddNode(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # runtime: O(n) where n is number of nodes
    def RemoveDuplicates(self):
        datas = set()
        prev_node = None
        cur_node = self.head
        while cur_node:
            if cur_node.data in datas:
                prev_node.next = cur_node.next   
            else:
                datas.add(cur_node.data)
                prev_node = cur_node
            cur_node = prev_node.next

# test functions
arr = [3,5,4,3,3,2,3,1]
linked_list = LinkedList(arr)
print(linked_list)
linked_list.RemoveDuplicates()
print(linked_list)
    

