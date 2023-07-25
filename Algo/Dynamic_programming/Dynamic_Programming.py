"""
DP 해결방법:
1. 크고 복잡한 문제를 하위 문제로 나눈다.
예) def fibo(n):
        return fibo(n-1)+fibo(n-2)

2. 하위 문제에 대한 답을 계산한다.
예) def fibo(n):
        if n == 1 or n == 2:
            return 1
        return fibo(n-1) + fibo(n-2)

3. 하위 문제에 대한 답으로 원래 문제에 대한 답을 계산한다.
memoization을 사용하면 시간복잡도 O(n), 안쓰면, O(2^n)

예) 
memo ={}
def fibo(n):
        if n == 1 or n == 2:
            return 1
        if n not in memo:
            memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]

        
        
DP에는 2가지 접근 방법이 있음:
- topdown or bottom up        

- topdown 의 경우 재귀를 사용
- bottomup의 경우 for loop을 사용
        
        
피보나치 topdown:
memo ={}
def fibo(n):
        if n == 1 or n == 2:
            return 1
        if n not in memo:
            memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]

피보나치 bottomup:
memo ={1:1, 2:1}
def fibo(n):
        for i in range(3,n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
        
     
"""