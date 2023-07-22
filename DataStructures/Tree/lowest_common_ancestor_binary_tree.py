"""
문제에서 Binary tree 하나와 해당 트리에 속한 두개의 노드가 주어진다. 
이때, 두 노드의 공통 조상중 가장 낮은 node, 즉, the lowest common ancestor 를 찾아라.


                1                 
          2            10        
       4     5       9     12    
     6   7         8         14   

Input: Binary tree, node1 = 2, node2 = 10
Output: lowest common ancestor = 1

Input: Binary tree, node1 = 8, node2 = 10
Output: lowest common ancestor = 10

구현:


"""

def LCA(root,p,q):
    # 만약 루트가 없으면 스킵
    if root == None:
        return None

    #recursive sequence
    left = LCA(root.left,p,q)
    right = LCA(root.right,p,q)

    #base case:
    if root == p or root == q:
        return root
    elif left and right:
        return root
    return left or right


