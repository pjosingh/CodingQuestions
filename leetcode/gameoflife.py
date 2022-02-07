import copy
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        copy_board = copy.deepcopy(board)

        for i in range(len(board)):
            for j in range(len(board[i])):
                res = self.check(board, i, j)
                
                if board[i][j] ==1 and res <2:
                    copy_board[i][j] = 0
                elif board[i][j] ==1 and (res == 2 or res == 3):
                    # 
                    copy_board[i][j] = 1
                elif board[i][j] ==1 and (res > 3):
                    copy_board[i][j] = 0
                elif board[i][j] ==0 and (res == 3):
                    copy_board[i][j] = 1

            
        return copy_board
    
    def check(self, board, i, j):
        neigh = [[0,1], [0,-1], [1,0], [1,-1], [1,1], [-1,-1], [-1,0], [-1,1]]
        count = 0
        for c in neigh:
            
            if self.is_valid(board, i+c[0], j+c[1]):
                if board[i+c[0]][j+c[1]] == 1:
                    count += 1
        return count

    def is_valid(self, board, i, j):
        if i>=0 and i<len(board) and j>=0 and j<len(board[i]):
            return True
        return False

sol = Solution()
print(sol.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))