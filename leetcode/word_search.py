class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.directional_search(board, word, i,j, 0):
                        return True
        
        return False

    def directional_search(self, board, word, i, j, index):
        # horizontal or vertical neighbours 
        n = len(board)
        m = len(board[0])

        if word == "":
            return True

        pos = [[-1,0], [1,0], [0,1], [0,-1]]
        
        for p in pos:
            if self.is_valid(n, m, i, j):
                if board[i][j] == word[index]:
                    temp = board[i][j]
                    board[i][j] = 0
                    self.directional_search(board, word, i, j, index+1)
                    board[i][j] = temp
        
        return False

    def is_valid(self, n, m, i, j):
        if i < n and j < m and i > 0 and j > 0:
            return True
        return False

sol = Solution()
assert sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED") == True