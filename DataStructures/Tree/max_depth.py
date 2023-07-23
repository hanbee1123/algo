"""
문제에서 binary tree가 주어진다. 주어진 binary tree의 최대깊이를 반환해라


문제접근법:
recursion을 이용한 접근법:

Idea is to perform a DFS. 
In case, the end node is met, return value 1.

current depth = max(left ,right)


코드구현:

def max_depth(root):
    if root.left == None and root.right == None:
        return 1
    
    left = root.left
    right = root.right

    return max(left, right)+1

"""

def max_depth(root):
    if root.left == None and root.right == None:
        return 1
    
    left = root.left
    right = root.right

    return max(left,right)+1

""""
코드구현 using BFS:
    max_depth = 0
    if root == None:
    return max_depth

    q.deque()
    q.append((root,1))

    while q:
        new_node, new_depth = q.popleft() 
        max_depth = max(max_depth, cur_depth)
        if 
        q.append((new_node.left, cur_depth + 1)
        q.append((new_node.right, cur_depth+1))

"""

from collections import deque

def using_bfs(root):
    if root == None:
        return 0

    q = deque()
    q.append((root, 1))


    while q:
        curr_node, curr_depth = q.popleft()
        max_depth = (max_depth, curr_depth)
        if curr_node.left:
            q.append(curr_node.left, curr_depth+1)
        if curr_node.right:
            q.append(curr_node.right, curr_depth+1)

    return max_depth