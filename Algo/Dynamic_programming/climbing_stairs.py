"""
계단을 올라가고 있다. 이 계단의 꼭대기에 도착하려면 n개의 steps만큼 올라가야 한다. 
한번 올라갈 때 마다 1step 또는 2steps 올라갈 수 있다.
꼭대기에 도달하는 방법의 갯수는 총 몇가지 일까요?

input: n=2
output = 2
1. 1+1
2. 2


input: n=3,
output =3
1. 1+1+1
2. 1+2
3. 2+1

DP using topdown
memo = {}
def dp_topdown(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    if n not in memo:
        memo[n] = dp_topdown(n-1) + dp_topdown(n-2)
    if n in memo:
        return memo[n]
    
    return dp_topdown(n-1) + dp_topdown(n-2)
DP using bottomup
"""

def dp_topdown(n):
    memo = {1:1, 2:2}
    def dp(n):
        if n not in memo:
            memo[n] = dp(n-1)+dp(n-2)
        return memo[n]
    dp(n)
    return memo[n]
    

def dp_bottomup(n):
    memo = {1:1, 2:2}
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]


if __name__ == "__main__":
    print(dp_topdown(5))
    print(dp_bottomup(5))