class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        
        '''
        [-5,1,5,0,-7]
        0
        -5
        -4
        1
        1
        -6

        [-4,-3,-2,-1,4,3,2]
        0
        -4
        -7
        -9
        -10
        -6
        -3
        -1


        '''

        max_value = 0
        current = 0

        for el in gain:
            current += el
            if current > max_value:
                max_value = current


        return max_value    
        

sol = Solution()
assert sol.largestAltitude([-5,1,5,0,-7]) == 1
assert sol.largestAltitude([-4,-3,-2,-1,4,3,2]) == 0