class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0
    
    def insert_head(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.node_count += 1
    
    def pop_head(self):
        if self.head == None:
            raise RuntimeError("The list is currently empty")
        elif self.node_count == 1:
            self.head = None
            self.tail = None
            self.node_count = 0
        else:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
            self.node_count -= 1
        
    def push(self, data):
        new_node = Node(data)
        ptr = self.head

        if self.head:
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node
            new_node.prev = ptr
        else:
            self.head = new_node
        self.node_count += 1
        self.tail = new_node
    
    def pop(self):
        if self.tail == None:
            raise RuntimeError('The list is currently empty')
        elif self.node_count == 1:
            self.head = None
            self.tail = None
            self.node_count == 0
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.node_count -= 1
    
    def insert_at(self,idx,data):
        new_node = Node(data)
        counter = 0
        ptr = self.head
        prev = ptr

        if idx < 1 or idx > self.node_count+1:
            raise RuntimeError(f"You currently have {self.node_count} nodes in your list")
        elif idx == 1:
            self.insert_head(data)
        elif idx == self.node_count + 1:
            self.push(data)
        else:
            while counter < idx-1:
                prev = ptr
                ptr = ptr.next
                counter += 1
            new_node.next = ptr
            new_node.prev = prev
            prev.next = new_node
            ptr.prev = new_node
            self.node_count += 1    
        
    def del_index(self, idx):       
        counter = 0
        ptr = self.head
        prev = ptr

        if idx < 1 or idx > self.node_count+1:
            raise IndexError(f"The current list consists of {self.node_count} nodes")
        elif idx == 1:
            self.pop_head()
        elif idx == self.node_count:
            self.pop()
        else:
            while counter < idx-1:
                counter += 1
                prev = ptr
                ptr = ptr.next
            prev.next = ptr.next
            ptr.next.prev = prev
            self.node_count -= 1

    def insert_before(self, idx, data):
        self.insert_at(idx-1, data)
    
    def insert_after(self, idx, data):
        self.insert_at(idx+1, data)
    
    def print_list(self):
        lister = []
        ptr = self.head
        while ptr:
            lister.append(ptr.data)
            ptr = ptr.next
        if len(lister) != 0:
            print(lister)
        else: 
            print("List is empty!")

if __name__ == "__main__":
    b = DList()
    b.insert_head(1)
    b.print_list()
    b.insert_head(0)
    b.print_list()
    b.push(2)
    b.print_list()
    b.insert_at(3,-1)
    b.print_list()
    b.pop()
    b.print_list()
    b.pop_head()
    b.print_list()
    b.insert_before(2,100)
    b.print_list()
    b.insert_after(3, 200)
    b.print_list()
    b.del_index(2)
    b.print_list()

