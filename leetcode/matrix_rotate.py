class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # first reverse the matrix 
        
        for i in range(int(len(matrix)/2)):
            if (i == len(matrix) - i - 1):
                continue

            list1 = matrix[i]
            list2 = matrix[len(matrix)-i-1]

            for j in range(len(list1)):
                temp = list1[j]
                list1[j] = list2[j]
                list2[j] = temp

        print(matrix)

        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        print (matrix)



sol = Solution()
sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])

