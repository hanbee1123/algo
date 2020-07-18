# Here are some terms for binary trees
# A binary tree has 2 childs max.
# 1. Parent, Child
# 2. Height, Depth
# 3. Degree
# 4. Full Binary tree (number of nodes  = 2^k -1)
# 5. Complete binary tree (When k-2 level is full and nodes exist in k-1 level)

# Functions to implement with binary trees are size, depth, traversal, 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BTree():
    def __init__(self, root):
        self.root = root
    
