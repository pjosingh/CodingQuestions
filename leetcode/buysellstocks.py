import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        high = -10000
        low = 10000
        profit = 0
        for el in range(len(prices)-1, -1, -1):
            if prices[el] > high:
                high = prices[el]
            
            if high != -10000 and prices[el] < low:
                low = prices[el]

            if high != -10000 and low != 10000 and prices[el] > low:
                profit += high-low
                high = -10000
                low = 10000
        
        return profit
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))

# 4 