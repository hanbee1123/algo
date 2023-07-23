"""
Number of Islands

지도에 표시된 섬들의 총 갯수를 반환하시오.
1은 땅, 0은 물

input = grid = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,1]
]

output = 2

문제접근법:
perform bfs from start. If not visited. keep performing bfs.
If bfs is reached, move to the second node and test visited.

코드구현:
for i in grid:
    if i is not in visited:
    perform bfs using deque.
    if all area has been reached, keep moving.

    numofislands += 1
"""


from collections import deque

def num_of_islands_bfs(grid):
    visited = []
    num_of_islands = 0 

    q = deque()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and (i,j) not in visited:
                num_of_islands += 1
                q.append((i,j))
                visited.append((i,j))

                while q:
                    r,c = q.popleft()
                    directions = [[-1,0],[1,0],[0,-1],[0,1]]

                    for dr, dc in directions:
                        row_pos = r+dr
                        col_pos = c+dc
                        if 0<=row_pos < len(grid) and 0<=col_pos<len(grid[0]) and grid[row_pos][col_pos] == '1' and (row_pos,col_pos) not in visited:
                            q.append((row_pos,col_pos))
                            visited.append((row_pos,col_pos))
                            
    return num_of_islands

def num_of_islands_dfs(grid):
    visited = []
    row_len = len(grid)
    col_len = len(grid[0])
    island_count = 0
    for i in range(row_len):
        for j in range(col_len):
            if (i,j) not in visited and grid[i][j] == '1':
                island_count += 1
                dfs(grid,i,j,visited)
    return island_count

def dfs(grid, row, col, visited):
    visited.append((row,col))

    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    for next_row, next_col in directions:
        new_row = row + next_row
        new_col = col + next_col

        if 0<=new_row<len(grid) and 0<=new_col<len(grid[0]) and grid[new_row][new_col] == '1' and (new_row,new_col) not in visited:
            dfs(grid, new_row, new_col, visited)

    return visited


if __name__ == "__main__":
    
    grid = [
        ["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],
        ["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],
        ["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],
        ["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],
        ["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],
        ["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],
        ["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],
        ["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],
        ["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],
        ["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],
        ["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],
        ["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],
        ["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],
        ["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],
        ["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],
        ["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],
        ["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],
        ["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],
        ["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],
        ["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]]
    print(num_of_islands_dfs(grid))
    print(num_of_islands_bfs(grid))