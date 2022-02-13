class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        direction = [[0,1], [1,0], [0,-1], [-1,0]]

        dir = 0

        i=0
        j=0
        res = []
        res.append(matrix[i][j])
        matrix[i][j] = -101

        direc = direction[dir]
        
        while len(res) != len(matrix) * len(matrix[0]):
            while i + direc[0] < len(matrix) and i + direc[0] >=0 and j+direc[1] >=0 and j+direc[1] < len(matrix[0]) and matrix[i + direc[0]][j+direc[1]] != -101:
                i = i + direc[0]
                j = j + direc[1]
                res.append(matrix[i][j])
                matrix[i][j] = -101

        
            dir += 1
            dir = dir%4
            direc = direction[dir]
        
        
        return res

            





sol = Solution()
assert sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]