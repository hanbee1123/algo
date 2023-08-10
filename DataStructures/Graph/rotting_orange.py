# 994. Rotting Oranges
# Medium
# 11.3K
# 356
# Companies
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# # Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        seen = set()
        fresh, new_fresh = 0,0
        q = deque()
        count = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,count))
                if grid[i][j] == 1:
                    fresh += 1
        while q:
            x,y,count = q.popleft()
            for d in directions:
                new_x = x+d[0]
                new_y = y+d[1]
                if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) and grid[new_x][new_y] == 1 and (new_x,new_y)not in seen:
                    q.append((new_x,new_y,count+1))
                    seen.add((new_x,new_y))
                    fresh -= 1

        if fresh != 0:
            return -1
        else:
            return count