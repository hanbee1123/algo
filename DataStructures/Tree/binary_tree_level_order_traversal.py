"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root):
        if root is None:
            return None
        q = deque()
        q.append(root)
        return_val=[]
        while q:
            size = len(q)
            print(size)
            val = []
            for i in range(size):
                cur_node = q.popleft()
                val.append(cur_node.val)
            
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

            return_val.append(val)

        return return_val