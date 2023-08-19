"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

"""

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        """
        Using BFS
        """
        if root is None:
            return []
        q = deque()
        q.append(root)
        final_result = []
        while q:
            lenth = len(q)
            for i in range(lenth):
                node = q.popleft()
                if i == lenth -1:
                    final_result.append(node.val)
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return final_result