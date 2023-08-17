# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
class Solution:
    def spiralOrder(self, matrix):
        """
        [1,1][1,2][1,3][1,4]
        [2,4]
        [3,4][3,3][3,2][3,1]
        [2,1][2,2][2,3]
        """

        output = []
        left,right,top,bottom = 0, len(matrix[0])-1, 0, len(matrix)-1 

        while left<=right and top<=bottom:
            for i in range(left, right+1):
                output.append(matrix[top][i])
            top += 1

            for j in range(top, bottom+1):
                output.append(matrix[j][right])
            right -= 1

            if left>right or top>bottom:
                break

            for k in range(right, left-1,-1):
                output.append(matrix[bottom][k])
            bottom -= 1

            for v in range(bottom, top-1,-1):
                output.append(matrix[v][left])
            left+=1

        return output