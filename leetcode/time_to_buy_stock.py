import sys 

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        print(prices)
        n = len(prices)
        max_value = 0
        min_value = sys.maxint
        total = 0
        
        for el in prices:
            if el < min_value:
                min_value = el

            if min_value != sys.maxint:
                if max_value > (el - min_value):
                    max_value = el - min_value
        


        

sol = Solution() 
assert sol.maxProfit([3,3,5,0,0,3,1,4]) == 6

