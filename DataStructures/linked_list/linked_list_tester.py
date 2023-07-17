class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LL():
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newnode

    def get(self,index):
        current = self.head
        for _ in range(index):
            current = current.next
        print(current.data)



    def printall(self):
        if self.head == None:
            print("No node")
        else:
            current = self.head
            while current:
                print(current.data, '==>')
                current = current.next


    def nodelength(self):
        if self.head == None:
            # print("No node")
            return 0
        else:
            counter = 0
            current = self.head
            while current:
                counter += 1
                current = current.next

            return counter
        


    def insert_at(self,idx,data):
        """
        For insert_at we must think of 3 scenarios.
        1. When requested index is higher than the total node count
        2. When input is done in the head, we must set the new node and head.
        3. When input is made in tail
        4. When the input is made between 2 nodes.
        """

        newnode = Node(data)


        #1. When requested index is higher than the total node count - Raise Error
        if self.nodelength() < idx:
            raise AttributeError(f"The requested index is longer than the total length of the node which is {self.nodelength()}")
            
        else:
            #2. When there is no node, set new node as head
            if self.head == None and idx == 0:
                self.head = newnode
            #2. When there is a node and index is 0, push all aside and set new node as head.
            elif self.head != None and idx == 0:
                newnode.next = self.head
                self.head = newnode

            #3. When input is made in tail
            elif self.nodelength() == idx:
                current = self.head
                while current.next != None:
                    current = current.next
                current.next = newnode
                return
            
            #4. When input is made between nodes
            else:
                current = self.head
                for _ in range(idx-1):
                    if current.next == None:
                        current.next = newnode
                    else:
                        current = current.next
                newnode.next = current.next
                current.next = newnode

if __name__ == "__main__":
    linked_list = LL()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.insert_at(1,99)
    linked_list.printall()
    print(f"Node length is {linked_list.nodelength()}")