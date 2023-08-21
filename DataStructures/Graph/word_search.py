"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

"""


class Solution:
    def exist(self, board, word):
        """
        Simply a DFS question
        We cannot tick of visited areas.
        Visited areas shall be visited again.
        """
        self.grids = [[-1,0],[1,0],[0,-1],[0,1]]
        print(word)
        self.board2 = board.copy()
        for m in self.board2:
            print(m)
        def dfs(word,i,j,board,previous):
            previous.append([i,j])
            print("")
            self.board2[i][j] = '-'
            for k in self.board2:
                print(k)
            if len(word) == 1:
                return True
            
            for x,y in self.grids:
                new_x = i+x
                new_y = j+y
                if 0<=new_x<len(board) and 0<=new_y<len(board[0]) and board[new_x][new_y] == word[1] and [new_x,new_y] not in previous:
                    if dfs(word[1:],new_x,new_y,board, previous):
                        return True
            
            previous.pop()
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(word,i,j,board,previous=[]):
                        return True
        return False

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    s = Solution()
    print(s.exist(board,word))