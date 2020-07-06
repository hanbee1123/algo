# Node class for doubly linked list
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.head.prev = None
        self.tail.next = None
        self.tail.prev = self.head
        self.node_count = 0
