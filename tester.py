from collections import deque
def updateMatrix(mat):
    """
    loop through matrix
    if matrix[x][y] is not 0:
        perform BFS (until 0 is met.)
        change matrix[x][y] to distance
    """
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                mat[i][j] = bfs(mat,i,j)
                #perform bfs and return lowest val. 
                #set mat[i][j] as lowest val
    return mat

def bfs(mat, i, j):
    visited = {}
    counter = 1
    q = deque([(i,j,counter)])
    directions = [[-1,0],[0,-1],[1,0],[0,1]]
    while q:
        row, col, new_counter = q.popleft()
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if 0<=new_row<len(mat) and 0<=new_col<len(mat[0]) and (new_row,new_col) not in visited:
                if mat[new_row][new_col] == 0:              
                    return new_counter
                else:
                    visited[(new_row,new_col)] = 'd'
                    q.append((new_row,new_col,new_counter+1))
    return counter

if __name__ == "__main__":
    matrix =[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]]
    print(updateMatrix(matrix))