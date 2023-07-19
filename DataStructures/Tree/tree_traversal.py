"""
트리 순회(traversal)이란 트리탐색 이라고 불리며 트리의 각 노드를 방문하는 과정을 말한다.
모든 노드를 한번 씩 방문해야 하므로 완전탐색이라고도 불린다. 순회방법으로는 
너비우선 탐색의 BFS와 깊이 우선 탐색의 DFS가 있다.

너비우선 탐색
         A
    B         C
D      E   F     H

A -> B -> C -> D -> E -> F -> G

"""
from collections import deque
def bfs(root):
    visited = []
    if root is None:
        return 0
    q = dequeu()
    q.append(root)
    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited
