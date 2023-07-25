"""
Min cost climbing stairs

계단을 올라가고 있다. 한번 올라갈 때마다 1step 또는 2step을 올라갈 수 있다.
문제에서 정수형 배열 cost가 주어지는데, cost[i]는 i번째 계단을 밟았을 때 지불해야하는 비용이다.

처음 시작은 index0 또는 index1중 한곳에서 시작할 수 있다.

이 계단의 꼭대기에 도착하기 위해 지불해야하는 비용의 최소값을 반환해라

input: cost = [10,15,20]
output:15

"""
#bottomup method
def dp_bfs(cost: list):
    memo = {}
    memo[0], memo[1] = cost[0], cost[1]
    for v in range(2,len(cost)):
        if v not in memo:
            memo[v] = cost[v] + min(memo[v-1],memo[v-2]) 
    return min(memo[len(cost)-1], memo[len(cost)-2])

#topdown method
def dp_dfs(cost:list):
    memo = {}
    memo[0], memo[1] = cost[0], cost[1]
    def dfs(n):
        if n == 0 or n==1:
            return memo[n]
        if n not in memo:
            memo[n] = cost[n]+min(dfs(n-1), dfs(n-2))
        return memo[n]


    return min(dfs(len(cost)-1),dfs(len(cost)-2))        



if __name__ == "__main__":
    cost = [1,15,20]
    print(dp_bfs(cost))
    print(dp_dfs(cost))