"""

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 
"""
from collections import deque, defaultdict
class Solution:
    def findMinHeightTrees(self, n, edges):
        #method using tree bfs
        hashmap = defaultdict(list)
        for edge in edges:
            hashmap[edge[0]].append(edge[1])
        for edge in edges:
            hashmap[edge[1]].append(edge[0])
        
        hashmap2 = {}
        for i in hashmap.keys():
            hashmap2[i] = self.depth_tree(i,hashmap)
        
        print(hashmap2)
        return min(hashmap2, key=hashmap2.get)

    def depth_tree(self, root, hashmap):
        seen = []
        q = deque([(root,0)])
        while q:
            x = q.popleft()
            cur_node = x[0]
            cur_depth = x[1]
            seen.append(cur_node)
            for j in hashmap[cur_node]:
                if j not in seen:
                    q.append((j,cur_depth+1))
        return cur_depth
    
if __name__ == "__main__":
    s = Solution()
    s.findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]])