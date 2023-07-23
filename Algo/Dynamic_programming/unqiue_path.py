"""
이 로봇은 m*n grid 위에 있습니다. 로봇은 처음에 좌측 상단 모서리 grid[0][0] 에 위치해 있습니다.
로봇은 우측 하단 모서리 grid[m-1][n-1] 으로 이동하려고 합니다.
로봇은 한번에 오른쪽이나 아래쪽으로만 움직일 수 있습니다.

두 정수 m,n이 주어졌을 때, 로봇이 우측하단 모서리에 도달할 수 있는 가능한 unqiue path 의 수를 반환하시오

input = (m=3, n=7)
output = 28

코드 구현:
    그냥 for loop:
    
    모두다 1인 grid 생성.
    1 1 1 1 1
    1 1 1 1 1
    1 1 1 1 1

    grid[1][1] 부터 시작해 grid[1][1]은 grid[0][1] + grid[1][0] 이다.
                          grid[1][2]는 grid[0][2] + grid[1][1] 이다.
    끝날 때까지 한다음에 
    마지막에 grid[-1][-1] 리턴하기

"""


#bottomup method using for loop
def path(rows: int, cols:int):
    grid = [[1]*cols for r in range(rows)]

    for row in range(1,rows):
        for col in range(1,cols):
            grid[row][col] = grid[row-1][col] + grid[row][col-1]
    return grid[-1][-1]



#top down method using recursion
def path_topdown(rows:int, cols:int):
    memo = {}
    for i in range(rows):
        memo[(i,0)] = 1
    for j in range(cols):
        memo[(0,j)] = 1

    def dp(r,c):
        if (r,c) not in memo:
            memo[(r,c)] = dp(r-1,c) + dp(r,c-1)
        return memo[(r,c)]
    
    dp(rows-1,cols-1)
    return memo[(rows-1,cols-1)]
    


if __name__ == "__main__":
    print(path(3,7))
    print(path_topdown(3,7))