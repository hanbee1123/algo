# Binary Search Tree vs Binary Search Array
# Tree: Easier to add or remove nodes
# Tree: Required more memory size.

# Type of binary trees are:
# 1. Full binary tree (When the number of nodes are 2^depth -1)
# 2. Complete binary tree (When the depth-2 level is full and there exist some nodes in depth-1 level)

# Functions to implement with binary search trees are (size, depth, traversal(inorder, preorder. postorder, breadth first traversal)
# insert(key,data), remove(key), in_order(), min(), max())

# Traversal types: Depth First Traversal, Breadth First Traversal
# Depth First Traversal has 
# 1. in-order traversal - left, self, right
# 2. pre-order traversal - self, left, right
# 3. post-order traversal -  left, right, self

# Breath First Traversal - visits the nodes in lower levels first then to the next levels.
# When nodes are in the same level, the same order is applied as their parents order.
# If they have the same parent, left is visited firs then right
# In order to use Breath First Traversal we must use queue


"""
The following code will implement the following binary tree:
                1                 ---> level 1
          2            10         ---> level 2
       4     5       9     12     ---> level 3
    6    7         8         14   ---> level 4

The features are as follows:
   - preoder: Perform a preorder traversal on the tree
   - inorder: Perform a inorder traversal on the tree
   - postorder: Perform a postorder traversal on the tree
   - bft: Perform a breadth first traversal on the tree
   - get_node: get a value from the node with a certain key value
   - insert: insert a node with a key and a value
   - get_max: get the value of the node with the max key
   - get_min: get the value of the node with the min key
   - get_height: get the height of the tree
   - get_count: count the number of nodes in the tree
   - delete: delete a node
"""


#array queue, insert, inorder postorder preorder bfs
# Array queue is implemented for the usage of bredth depth first traversal
class ArrayQueue:
    def __init__(self):
        self.data = []
    def enqueue(self,data):
        self.data.append(data)
    def dequeue(self):
        return self.data.pop(0)
    def peek(self):
        return self.data[0]
    def size(self):
        return len(self.data)
    def is_empty(self):
        return self.size() == 0
    
class BSNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    
    def __repr__(self):
        return print(f'The key is {self.key} and the value is {self.data}')

class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        new_node = BSNode(key, data)
        if self.root:
            ptr = self.root
            while True:
                if key > ptr.key:
                    if ptr.right == None:
                        ptr.right = new_node
                        break
                    else:
                        ptr = ptr.right
                elif key < ptr.key:
                    if ptr.left == None:
                        ptr.left = new_node
                        break
                    else: 
                        ptr = ptr.left
                else:
                    raise KeyError("You have the same key value in your tree!")
        else:
            self.root = new_node

    def in_order(self, node):
        if node == None:
            return
        else:
            self.in_order(node.left)
            print(node.key)
            self.in_order(node.right)
    
    def pre_order(self, node):
        if node == None:
            return
        else: 
            print(node.key)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node == None:
            return
        else:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.key)
    
    def bft(self, node):
        queue = ArrayQueue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            node = queue.dequeue()
            print(node.key)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
    
    def delete_node(self, key):
        #There are 3 cases when deleting a node
        # 1. When the node is an edge (has no child)
        # 2. When the node has one child
        # 3. When the node has two childs
        
        # If root node does not exist raise value error
        if self.root == None:
            return ValueError("There is no node in the tree")
        # First find the node to be deleted.
        else:
            ptr = self.root
            parent = self.root
            check = False
            while ptr:
                if ptr.key == key:
                    check = True
                    break
                elif key < ptr.key:
                    parent = ptr
                    ptr = ptr.left
                else: # key > ptr.key:
                    parent = ptr
                    ptr = ptr.right
            
            if check == False:
                return ValueError(f"There is no node in the tree with the key value {key}")

            # Case 1 : Node has no child
            if ptr.left == None and ptr.right == None:
                if key < parent.key:
                    parent.left == None
                else:
                    parent.right == None
            # Case 2: node has one child
            elif ptr.left != None and ptr.right == None:
                if key < parent.key:
                    parent.left = ptr.left
                else:
                    parent.right = ptr.right
            # Case 3: node has 2 children
            
            
            

if __name__ == "__main__":
    a = BSTree()
    a.insert(5,5)
    a.insert(3,3)
    a.insert(7,7)
    a.insert(4,4)
    a.insert(2,2)
    a.insert(6,6)
    a.insert(8,8)


    a.in_order(a.root) 
    print("\t")
    a.post_order(a.root) 
    print("\t")
    a.pre_order(a.root) 
    print("\t")
    a.bft(a.root)
    a.delete_node(5)
    a.bft(a.root)

