import time

class Solution(object):
    def exist(self, board, word):
        t1 = time.perf_counter()
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if self.directional_search(board, word, i,j, 1, n,m):
                        return True
        t2 = time.perf_counter()
        print(f"Run in {t2 - t1:0.10f} seconds")
        return False

    def directional_search(self, board, word, i, j, index, n,m ):

        #print("\t", board, word, i, j, index)

        if len(word) == index:
            return True

        pos = [[-1,0], [1,0], [0,1], [0,-1]]
        temp = board[i][j]
        board[i][j] = 0

        for p in pos:
            
            if i+p[0] < n and j+p[1] < m and i+p[0] >= 0 and j+p[1] >= 0 and board[i+p[0]][j+p[1]] != 0 and board[i+p[0]][j+p[1]] == word[index]:
            #if self.is_valid(n, m, i+p[0], j+p[1]):
            #    if board[i+p[0]][j+p[1]] == word[index]:
                if self.directional_search(board, word, i+p[0], j+p[1], index+1, n, m):
                    return True
                    
        board[i][j] = temp

        return False

sol = Solution()
assert sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED") == True
assert sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE") == True
assert sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") == False