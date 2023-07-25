import heapq
def djikstra(graph,start,final,n):
    costs = {}
    pq = []
    heapq.heappush(pq,(0,start))
    while pq:
        cur_cost , cur_v = heapq.heappop(pq)
        if costs[cur_v] < cur_cost:
            continue
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq,(next_cost,next_v))
    
    if len(costs) == N:
        return costs[final]
    else:
        return -1