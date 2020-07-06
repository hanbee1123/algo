class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def append(self, data):
        # if linked list is empty, head and tail is the new node
        new_node = Node(data)
        if self.node_count == 0:
            self.head = new_node
            self.tail = new_node
        # If list is not empty, new node comes after the tail and new node becomes the tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.node_count += 1

    def pop(self):
        # If linked list contains of one node, set head and tail as none
        if self.node_count == 1:
            self.head = None
            self.tail = None
            self.node_count = 0
        # If linked list is empty raise value error
        elif self.node_count == 0:
            raise ValueError("Your Linked List is empty. There's no node to pop")

        else:
            pointer = self.head
            counter = 1
            while counter < self.node_count -1:
                pointer = pointer.next
                counter += 1
            prev = pointer
            self.tail = prev
            prev.next = None
            self.node_count -= 1
    
    def print_values(self):
        counter = 0
        ptr = self.head
        
        if self.node_count !=0:
            while ptr:
                print(ptr.data)
                ptr = ptr.next
                counter+=1
        else :
            raise ValueError("The linked list is empty. You have no node to print")

    def put_at(self, position, data):
        new_node = Node(data)

        # when position is higher than node_count raise error
        if position > self.node_count +1:
            raise AttributeError(f"The current length of the list is {self.node_count}.")
        #else, put the node in the position
        else:
            # if, node count is 0, new_node becomes head and tail
            if self.node_count == 0:
                self.head = new_node
                self.tail = new_node
            # if position is 1, new_node becomes head
            elif position == 1:
                new_node.next = self.head
                self.head = new_node
            # if position is node_count +1, new_node becomes tail
            elif position == self.node_count+1:
                self.tail.next = new_node
                self.tail = new_node
            # else, put the new_node between data
            else:
                ptr = self.head
                counter = 2
                while counter < position:
                    ptr = ptr.next
                    counter += 1
                new_node.next = ptr.next
                ptr.next = new_node
            #finally increment node_count by one
            self.node_count +=1

    def pop_head(self):
        # If node count is 0 then return value error
        if self.node_count == 0: 
            raise ValueError("The list is empty, there's no head to pop")
        # If node count is 1 then make list empty
        elif self.node_count == 1:
            self.head = None
            self.tail = None
            self.node_count -= 1
        # Else, delete head and shift it
        else:
            self.head = self.head.next
            self.node_count -=1
   
    def get_to(self,num):
        ptr = self.head
        if num == 0:
            raise ValueError("Can't put 0, the that doesn't return anything dumb dumb!")
        elif num > self.node_count:
            raise ValueError(f"The value you put is longer than the node. The max lenght is {self.node_count}")
        else:
            counter = 1
            while counter < num:
                ptr = ptr.next
                counter += 1
            return ptr.data

    def delete_values(self, data):
        ptr = self.head
        prev = Node('dummy')
        prev.next = ptr
        while ptr != None:
        # if value is at head pop_head
            if ptr == self.head and ptr.data == data:
                self.pop_head()
                ptr = self.head
                prev.next = ptr

        #if value is at tail pop_tail
            elif ptr == self.tail and ptr.data == data:
                 self.pop()
                 ptr = self.tail
        
        # if value is between head and tail
            elif ptr.data == data:
                prev.next = ptr.next
                ptr = prev.next
                self.node_count -= 1
        
            else:
                ptr = ptr.next
                prev = prev.next

if __name__ == "__main__":
    LL = LL()
    LL.append(2000)
    LL.append(2000)
    LL.append(20)
    LL.append(2000)
    LL.append(30)
    LL.append(2000)
    LL.append(2000)
    LL.append('bee')
    LL.append(2000)
    LL.append(20)
    LL.append(20)
    
    LL.append(2000)
    LL.append(2000)

    LL.delete_values(2000)
    LL.delete_values(20)


    LL.print_values()

    
    
    # i_nums = iter(LL)
    # print(next(i_nums))
    # print(next(i_nums))    