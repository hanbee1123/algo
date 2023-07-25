#1. Tree Traversal BFS
from collections import deque
def bfs(root):
    if root is None:
        return None
    visited = []
    q = deque(root)
    while q:
        cur_node = q.popleft()
        visited.append(cur_node.val)
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)

    return visited


#2. Tree Traversal DFS (preorder, inorder, postorder)
def dfs_preorder(root):
    if root == None:
        return
    print(root.val)
    dfs_preorder(root.left)
    dfs_preorder(root.right)

def dfs_inorder(root):
    if root is None:
        return
    dfs_inorder(root.left)
    print(root.val)
    dfs_inorder(root.right)

def dfs_postorder(root):
    if root is None:
        return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.val)

#3. Graph Traversal BFS
    # graph = {
    #     'A':['B','D','E'],
    #     'B':['A','C','D'],
    #     'C':['B'],
    #     'D':['A','B'],
    #     'E':['A']
    # }

def bfs(graph, start_point):
    if graph is None:
        return None
    visited = [start_point]
    q = deque(start_point)
    while q:
        for v in graph[start_point]:
            if v not in visited:
                visited.append(v)
                q.append(v)
    return visited

def dfs(graph, start_point, visited=[]):
    visited.append(start_point)
    for v in graph[start_point]:
        if v not in visited:
            dfs(graph, v, visited)
    return visited


# dp topdown
#dp bottom up

def topdown(n):
    memo = {}
    def dp(n):
        if n==0 or n==1: return 1
        if n not in memo:
            memo[n] = dp(n-1)+dp(n-2)
        return memo[n]
    dp(10)
    return memo[n]

def bottomup(n):
    memo ={1:1,2:1}
    for v in range(3,n):
        memo[v] = memo[v-1] + memo[v-2]
    
    return memo[n]


if __name__ == "__main__":
    
    graph = {
        'A':['B','D','E'],
        'B':['A','C','D'],
        'C':['B'],
        'D':['A','B'],
        'E':['A']
    }

    print(dfs(graph,'A'))