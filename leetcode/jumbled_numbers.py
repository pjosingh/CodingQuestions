import sys


class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        temp = num
        nums = []
        while temp!=0:
            nums.append(temp%10)
            temp = int(temp/10)
            
        
        print(nums)

        self.create_numbers(nums)
        
    
    def create_numbers(self, nums):
        
        # single
        sum = sys.maxsize
        for i in range(4):
            for j in range(i+1, 4):
                print(i,j)
                if nums[i] + nums[j] < sum:
                    print(nums[i], nums[j], sum)
                    sum = nums[i] + nums[j]
         
        print(sum)
        
        
        # double 
        
        # tripple

sol = Solution()
sol.minimumSum(2932)