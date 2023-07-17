''' 
There exist a triangle that looks as the following
                7
            3       8
        8       1       0
    2       7       4       4
4       5       2       6       5

Imagine this as a tree and the node can only move to the left child or the right child.
If input is given as the following, 
Return the maximum value of path from top to bottom
'''

# For this quesiton we can use dynamic programming in two approaches
# 1. Bottom up DP
# 2. Top down DP

def bottom_up(triangle):
    # create a memoization
    memo = []
    def helper(row, col):
        #if value is seen in memo, dont loop through but just return value in memo
        if [row,col] in memo:
            return triangle[row][col]
        # End case
        if row == len(triangle)-1:
            return triangle[row][col]

        # Loop through
        for col_num in range(len(triangle[row])):
            triangle[row][col_num] += max(helper(row+1, col_num), helper(row+1,col_num+1))
            memo.append([row, col_num])
        return triangle[row][0]
    
    helper(0,0)
    
    for i in triangle:
        print(i)
        
    return triangle[0][0]

def top_down(triangle):
    row = len(triangle)
    for i in range(1,row):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    for i in triangle:
        print(i)

    return max(triangle[-1])
if __name__ == "__main__":
    triangle = [
                [7], 
                [3, 8], 
                [8, 1, 0],
                [2, 7, 4, 4], 
                [4, 5, 2, 6, 5]]	
    # bottom_up(triangle)
    # assert(bottom_up(triangle)==30)
    assert(top_down(triangle)==30)