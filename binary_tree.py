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
    
    def min_val_node(node):
        current = node
        while current.left != None:
            current = current.left
        return current


    def delete(self, root, key):
        if root == None:
            return KeyError("There is no root to this tree")
        if root.key > key:
            root.left = delete(root.left, key)
        elif root.key < key:
            root.right = delete(root.right, key)
        else: 
            # Delete node with one child or no child
            if root.left == None:
                temp = root.right
                root = None
                return temp
            elif root.right == None:
                temp = root.left
                root = None
                return temp
            # If the node has two children
            temp = min_val_node(root.right)
            root.key = temp.key
            root.right = delete(root.right, temp.key)
        return root














        def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else: 
                        parent.right = None
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    node = node.left
                else:
                    node = node.right
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if parent.left == node:
                        parent.left = node
                    else: 
                        parent.right = node
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = node
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    parent = successor
                    successor = successor.left
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                if parent.left == successor:
                    parent.left = successor.left
                else: 
                    parent.right = successor.right

            return True

        else:
            return False


























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
            elif ptr.left != None and ptr.right != None:
                curr_node = ptr.right
                curr_node_parent = ptr.right
                while curr_node.left == None:
                    curr_node_parent = curr_node
                    curr_node = curr_node.left
                ptr.key = curr_node.key
                ptr.data = curr_node.data
      

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

