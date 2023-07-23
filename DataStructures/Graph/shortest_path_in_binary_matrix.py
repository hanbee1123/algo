"""
n*n binary matrix인 grid가 주어졌을 때, 출발지에서 목적지까지 도착하는 가장 빠른 경로의 길이를 반환하시오. 만약 경로가 없다면 -1을 반환하시요.

출발지: top-left cell
목적지: bottom - right cell

-값이 0인 cell만 지나갈 수 있음.
-cell 끼리는 8가지 방향으로 연결되어있음.
-연결된 cell을 통해서만 나갈 수 있다. 


input : grid = [
    [0,0,0],
    [1,1,0],
    [1.1,0]
]

output: 4

코드설계:

bfs 로 설계:
    grid[0][0] 에서 시작해서, next가 0이면, queue에 next path and depth 추가.
    
    complete this until grid[last][last] is met.
    return depth


"""

from collections import deque
def bfs(grid):
    grid_length = len(grid)
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    
    visited = {}
    visited[(0,0)] = 'd'
    q = deque([(0,0,1)])
    directions = [(-1,0),(1,0),(1,1),(-1,1),(1,-1),(-1,-1),(0,-1),(0,1)]

    while q:
        cur_x, cur_y, cur_depth = q.popleft()
        if cur_x == grid_length-1 and cur_y == grid_length-1:
            return cur_depth
        
        for d in directions:
            x,y = d
            new_x = cur_x+x
            new_y = cur_y+y
            if 0 <= new_x < grid_length and 0<=new_y<grid_length and grid[new_x][new_y] == 0 and (new_x,new_y) not in visited:
                visited[(new_x,new_y)] = 'd'
                q.append((new_x,new_y,cur_depth+1)) 

    return -1

if __name__ == "__main__":
    grid = [
        [0,0,0],
        [1,1,0],
        [1,1,0]
        ]
    print(bfs(grid))


