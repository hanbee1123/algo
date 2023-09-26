"""
You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges times[i] = (ui,vi,wi) 
ui is the source node, 
vi is the target node
wi is the time it takes for a signal to travel from source to target

We will send a signal from a given node k.
Return the minimum time it takes for all the n nodes to receive the signal.
if it is impossible for all the n nodes to receive the signal return -1.


Input : times[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2
output : 2
"""

import heapq
def ndt(times,N,K):
        graph = {}
        for (u, v, w) in times:
            graph[u] = [(v, w)]
            
        priority_queue = [(0, K)]
        shortest_path = {}
        while priority_queue:
            w, v = heapq.heappop(priority_queue)
            if v not in shortest_path:
                shortest_path[v] = w
                for v_i, w_i in graph[v]:
                    heapq.heappush(priority_queue, (w + w_i, v_i))
                    
        if len(shortest_path) == N:
            return max(shortest_path.values())
        else:
            return -1
if __name__ =="__main__":
    print(ndt([[1,2,1],[2,1,3]], 2, 2))
    print('aasb')
    #tster