class Solution(object):
    def uniquePaths(self, m, n):
  
        global count 
        return self.move(m,n, 0,0)
                
        

    def move(self, m,n, i, j):
        dp = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(1)
            dp.append(temp)
                        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

sol = Solution()
print(sol.uniquePaths(3, 2))
print(sol.uniquePaths(3, 7))