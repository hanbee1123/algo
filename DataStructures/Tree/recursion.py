"""
재귀함수의 시간복잡도:
재귀함수의 전체 시간복잡도 = 재쉬 함수 호출 수 * 재귀 함수 하나당 시간 복잡도

O(n)n에 비례한 호출
recurrence relation = f(n) = f(n-1) + n  
ex. factorial 뿌리가 하나씩 나옴.


O(2^n)2^N 에 비례한 호출
recurrence relation = f(n) = f(n-1) + f(n-2)
ex. fibonacci 뿌리가 2개씩 나옴

O(log_2 n)
Binary search
"""


def factorial(n):
    if n==1:
        return 1
    return factorial(n-1) * n

def fibo(n):
    if n == 1 or 2:
        return 1
    return fibo(n-2) + fibo(n-1)


if __name__ == "__main__":
    print()
