import copy
class Solution(object):
    def uniquePathsIII(self, grid):

        def findPath(grid, starti, startj, ans, ansSet, zeroCount):
            
            if (starti <0 or startj<0):
                return
            if (starti >= len(grid) or startj >= len(grid[starti])):
                return

            
            if (grid[starti][startj] == 2):
                ans.append([starti, startj])
                #ans = ans +",["+starti+","+startj+"]"
                response = ""
                for el in ans:
                    response = response + "["+str(el[0])+","+str(el[1])+"]"
                if (zeroCount == 0):
                    ansSet.add(response)
                
                return
            if grid[starti][startj] == 0:
                zeroCount = zeroCount-1
            
            grid[starti][startj] = -1
            ans.append([starti, startj])
            cord = [[-1,0], [1,0] , [0,1], [0, -1]]
            
            for c in range(len(cord)):
                
                if (cord[c][0]+starti < len(grid) and cord[c][1]+startj < len(grid[starti])):
                    if (grid[cord[c][0]+starti][cord[c][1]+startj] != -1):
                        backupgrid = grid[cord[c][0]+starti][cord[c][1]+startj]
                        findPath(grid, cord[c][0]+starti, cord[c][1]+startj, ans, ansSet, zeroCount)
                        
                        if ([cord[c][0] + starti, cord[c][1] + startj] in ans):
                            ans.remove([cord[c][0] + starti , cord[c][1] + startj])
                            grid[cord[c][0]+starti][cord[c][1]+startj] = backupgrid
                        
                            
        #print(grid)
        
        starti = 0
        startj = 0

        zeroCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 1):
                    starti=i
                    startj=j
                if (grid[i][j] == 0):
                    zeroCount = zeroCount + 1

        ansSet = set()
        findPath(grid, starti, startj, [], ansSet, zeroCount)
        #print(ansSet)
        #print(len(ansSet))
        return len(ansSet)