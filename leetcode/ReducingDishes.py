

from audioop import reverse


class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        
        if len(satisfaction) == 0:
            return 0
        satisfaction.sort()
        return self.maxUtil(satisfaction, 0, 1, 0)
    
    def maxUtil(self, satisfaction, current_index, current_multiplier, current_sum):
        print("call stack: ", satisfaction, current_index, current_multiplier, current_sum)
        # ending condition 
        if current_index == len(satisfaction):
            return current_sum

        # taking the current_index
        taking = current_sum + current_multiplier* satisfaction[current_index]

        # not taking the current_index
        not_taking = current_sum
        
        taking =  self.maxUtil(satisfaction, current_index+1, current_multiplier+1, taking)
        not_taking =  self.maxUtil(satisfaction, current_index+1, current_multiplier, not_taking)
        
        return max(taking, not_taking, 0)
        

sol = Solution()
print(sol.maxSatisfaction([-1,-8,0,5,-9]))
print(sol.maxSatisfaction([4,3,2]))
print(sol.maxSatisfaction([-1,-4,-5]))
#print(sol.maxSatisfaction([34,-27,-49,-6,65,70,72,-37,-57,92,-72,36,6,-91,18,61,77,-91,5,64,-16,5,20,-60,-94,-15,-23,-10,-61,27,89,38,46,57,33,94,-79,43,-67,-73,-39,72,-52,13,65,-82,26,69,67]))