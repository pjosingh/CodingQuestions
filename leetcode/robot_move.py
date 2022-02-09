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

        print(visited, m, n)

        self.move(m,n, 0,0, visited, [])

        return count
        
        
    count = 0

    def move(self, m,n, i, j, visited, path):
        global count
        
        #print(i, j, "path:", path, "visited:", visited)
        if i >= m or j >= n:
            return

        if i == m-1 and j == n-1:

            count += 1
            #print(path, count)
            #print(count)
            return
        
        # # if visited[i][j] == 1:
        # #     return
        
        # visited[i][j] = 1
        path.append([i,j])

        #print(visited)
        self.move(m,n, i+1,j, visited[:], path[:])
        self.move(m,n, i, j+1, visited[:], path[:])



sol = Solution()
print("Output: ", sol.uniquePaths(3,2))
print("Output: ", sol.uniquePaths(3,7))