"""
Graph에도 
BFS, DFS의 방법으로 traversal이 가능하다.


"""
"""
BFS공식은 그냥 외우자
"""
graph = {
    'A':['B','D','E'],
    'B':['A','C','D'],
    'C':['B'],
    'D':['A','B'],
    'E':['A']
}

from collections import deque
def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited


"""
DFS 그냥 외워버려야한다. 
"""


def dfs(graph, cur_v, visited=[]):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            visited = dfs(graph,v,visited)
    return visited

#또는 visted를 전역변수로 둬본다
visited=[]
def dfs2(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)
    