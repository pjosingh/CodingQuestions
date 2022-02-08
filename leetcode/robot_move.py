class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        global count 
        
        count = 0
        
        visited = []
        for i in range(m):
            current = []
            for j in range(n):
                current.append(0)
            visited.append(current)

        print(visited)
        self.move(m,n, 0,0, visited)

        return count
        
        
    count = 0

    def move(self, m,n, i, j, visited):
        global count
        
        if i >= m or j >= n:
            return

        if i == m-1 and j == n-1:

            count += 1
            print(count)
            return
        
        if visited[i][j] == 1:
            return
        
        visited[i][j] = 1

        print(visited)
        self.move(m,n, i+1,j, visited[:])
        self.move(m,n, i, j+1, visited[:])



sol = Solution()
print(sol.uniquePaths(3,2))