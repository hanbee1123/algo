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

#BFS 는 que가 쓰인다는걸 그냥 외워야한다. 
#아래 코드를 그냥 통째로 외우길 추천.
from collections import deque
def bfs(root):
    
    #초기 세팅
    visited = [] #순회를 하며 노드의 값들을 저장
    if root is None:
        return 0
    q = deque()  #방문할 노드의 순서를 저장하는 용도
    q.append(root)

    
    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

"""

DFS (Depth First Search)는 스택을 이용하거나 Recursion을 이용해서 구현할 수 있다.
 DFS 로 접근하는 방법은 크게 
 전위순회 (preorder)
 중위 순회 (inorder)
 후위 순회 (postorder)가 있다.

            A 
        B       C
     D     E  F    G
       H


preorder : A -> B -> D -> H -> E -> C -> F -> G
나 먼저 찍고
inorder : H -> D -> B -> E -> A -> F -> C -> G
왼쪽돌고 나 찍고
postorder : H -> D -> E -> B -> F -> G -> C -> A
다 돌고 나 찍고


Preorder, inorder, postorder 가는 방향은 같은데, 어떤걸 먼저 찍느냐가 다르다.

"""


def dfs_preorder(node):
    if node is None:
        return
    else:
        print(node.value)
        dfs(node.left)
        dfs(node.right)

def dfs_inorder(node):
    if node is None:
        return
    else:
        dfs(node.left)
        print(node.value)
        dfs(node.right)

def dfs_postorder(node):
    if node is None:
        return
    else:  
        dfs(node.left)
        dfs(node.right)
        print(node.value)