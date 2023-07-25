#1. Tree Traversal BFS, DFS
from collections import deque

def bfs(root):
    if root == None:
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
    

def dfs_preorder(root):
    if root == None:
        return
    print(root.val)
    dfs_preorder(root.left)
    dfs_preorder(root.right)


#2. Graph Traversal
def bfs_graph(graph,start):
    visited = []
    q = deque(start)

    while q:
        cur_node = q.popleft()
        visited.append(cur_node)
        for j in graph[cur_node]:
            if j not in visited:
                q.append(j)
    return visited

def dfs_graph(graph,start,visited=[]):
    visited.append(start)
    for j in graph[start]:
        if j not in visited:
            dfs_graph(graph,j,visited)
    return


#3. dynamic programming bottomup, topdown

def dp_bottomup(n):
    values = {1:1, 2:1}
    for i in range(3,n):
        values[i] = values[i-1]+values[i-2]
    return values[n]

def dp_topdown(n):
    memo = {}
    def dp(n):
        if n not in memo:
            memo[n] = dp(n-1) + dp(n-2)
        else:
            memo[n]
    
    dp(n)
    return memo[n]



    # graph = {
    #     'A':['B','D','E'],
    #     'B':['A','C','D'],
    #     'C':['B'],
    #     'D':['A','B'],
    #     'E':['A']
    # }



if __name__ == "__main__":
    
    graph = {
        'A':['B','D','E'],
        'B':['A','C','D'],
        'C':['B'],
        'D':['A','B'],
        'E':['A']
    }

    print(dfs(graph,'A'))