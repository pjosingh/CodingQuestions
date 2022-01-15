
class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        total = res = 0

        satisfaction.sort()
        while satisfaction and satisfaction[-1] + total > 0:
            pop = satisfaction.pop()
            print("stack trace 1: ", satisfaction, total, res, pop)
            total += pop
            res += total
            print("stack trace 2: ", satisfaction, total, res)

        return res

   

sol = Solution()
print(sol.maxSatisfaction([-1,-8,0,5,-9]))
print(sol.maxSatisfaction([4,3,2]))
print(sol.maxSatisfaction([-1,-4,-5]))
#print(sol.maxSatisfaction([34,-27,-49,-6,65,70,72,-37,-57,92,-72,36,6,-91,18,61,77,-91,5,64,-16,5,20,-60,-94,-15,-23,-10,-61,27,89,38,46,57,33,94,-79,43,-67,-73,-39,72,-52,13,65,-82,26,69,67]))