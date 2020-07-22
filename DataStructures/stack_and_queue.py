from doubly_linked_list import DList, Node

class ArrayStack:
    def __init__(self):
        self.data = []
    def push(self,data):
        self.data.append(data)
    def pop(self):
        return self.data.pop()
    def peek(self):
        return self.data[-1]
    def size(self):
        return len(self.data)
    def is_empty(self):
        return self.size() == 0

class ArrayQueue:
    def __init__(self):
        self.data = []
    def enqueue(self, data):
        self.data.append(data)
    def dequeue(self):
        self.data.pop(0)
    def peek(self):
        return self.data[0]
    def size(self):
        return len(self.data)
    def is_empty(self):
        return self.size() == 0

# In a circular queue there is a limit to the number of resources available
# functions are enqueue, dequeue, size, is_empty, is_full, peek
# location of front and rear changes constantly
class CircularQueue:
    def __init__(self, n):
        self.max_count = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1
    
    def size(self):
        return self.count
    
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.max_count
    
    def enqueue(self, data):
        if self.is_full:
            return IndexError("The Queue is full dumb dumb")
        self.rear = (self.rear+1) % self.max_count
        self.data[self.rear] = data
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The Queue is empty dumb dumb")
        self.front = (self.front+1) % self.max_count
        x = self.data[self.front]
        self.count -= 1
        return x
    
    def peek(self):
        return self.data[(self.front)%self.max_count]

#In a priority queue, the queue does not follow FIFO but rather each nodes have a priority of numbers and it pops accordingly to that priority.
# For example if a rule is to give higher priority to lower numbers
# enqueue would be 6 --> 5 --> 2 -->9
# dequeue would be 2 --> 5 --> 6 -->9

# There are two methods for doing priority queues
# 1. enqueue data according to priority in the first place (Enqueue 할 때, 우선순위를 유지하도록 설정)
# 2. Dequeue data according to priority (Dequeue 할 때, 우선순위를 유지하도록 설정)
# 1st is the better option. Because if data is in order, you can perform binary search and put
# For the 2nd option the time complexity is O(n)*max_count

# You can create a priority queue using both doubly linked list and array
# array uses less memory
# But linked_list has lower time complexity as data does not have to be shifted to be put into the middle
class PriorityQueue:
    def __init__(self):
        self.queue = DList()

    def is_empty(self):
        return self.queue.node_count == 0
    
    def size(self):
        return self.queue.node_count

    def enqueue(self, data):
        curr = self.queue.head
        counter = 1

        if curr == None or data < self.queue.head.data:
            self.queue.insert_head(data)
        else:
            while curr.data < data and curr.next != None:
                curr = curr.next
                counter += 1 
            if curr.data > data and curr.next == None:
                self.queue.insert_at(counter, data)
            elif curr.data < data and curr.next == None:
                self.queue.insert_after(counter, data)
            else:
                self.queue.insert_at(counter, data)

    def dequeue(self, data):
        self.queue.pop_head()
    
    def peek(self):
        return self.queue.head.data
    

if __name__ == "__main__":
    b = PriorityQueue()
    b.enqueue(5)
    b.enqueue(2)
    b.enqueue(100)
    b.enqueue(10)
    b.enqueue(11)
    b.enqueue(10)
    b.enqueue(2)
    b.enqueue(1)

    b.queue.print_list()