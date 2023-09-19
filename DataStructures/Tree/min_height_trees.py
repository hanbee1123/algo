# # 310. Minimum Height Trees
# # Medium
# # 7.2K
# # 295
# # Companies

# # A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

# # Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# # Return a list of all MHTs' root labels. You can return the answer in any order.

# # The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

# https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return[0]

        #step 1. change list to adjacency list
        adj_list = defaultdict(list)
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        leaves = [i for i in range(n) if len(adj_list[i]) == 1]

        #step 2. remove all edges until we have 1 or 2 nodes left
        while n > 2:
            #reduce num of nodes
            n -= len(leaves)
            new_leaves=[]
            #remove leaves
            for leave in leaves:
                neighbor = adj_list[leave].pop()
                adj_list[neighbor].remove(leave)
        
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves
        
        return leaves
