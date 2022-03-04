

class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        count = 0
        while count != 4:
            if not self.isEqual(mat, target):
                print("checking equal ", mat, target)
                mat = self.rotate(mat)
                print("Rotated: ", mat)
                count += 1
            else:
                return True
        return False

    def isEqual(self, mat, target):
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] != target[i][j]:
                    return False
        return True



    def rotateStep1(self, mat):
        for i in range(int(len(mat)/2)):
            for j in range(len(mat[i])):
                
                temp = mat[i][j]
                mat[i][j] = mat[len(mat[i])-1-i][j]
                mat[len(mat[i])-1-i][j] = temp
        return mat

    def rotateStep2(self, mat):

        for i in range(len(mat)):
            for j in range(i, len(mat[i])):
                if i == j:
                    continue

                temp = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = temp

        return mat



    def rotate(self, mat):
        mat = self.rotateStep1(mat)
        return self.rotateStep2(mat)

assert Solution().rotateStep1([[1,0,0],[1,0,1],[0,0,1]]) == [[0,0,1], [1,0,1], [1,0,0]]
assert Solution().rotateStep2([[0,0,1], [1,0,1], [1,0,0]]) == [[0,1,1],[0,0,0],[1,1,0]]

assert Solution().rotate([[0,0],[0,1]]) == [[0,0],[1,0]]
#assert Solution().rotate([[1,0,0],[1,0,1],[0,0,1]]) == [[0,1,1],[0,0,0],[1,1,0]]

assert Solution().findRotation(mat = [[0,1],[1,0]], target = [[1,0],[0,1]]) == True
assert Solution().findRotation(mat = [[0,1],[1,1]], target = [[1,0],[0,1]]) == False
assert Solution().findRotation(mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]) == True
assert Solution().findRotation([[0,0],[0,1]], [[0,0],[1,0]]) == True

assert Solution().findRotation([[1,0,0],[1,0,1],[0,0,1]],[[0,1,1],[0,0,0],[1,1,0]]) == True