import time

class Solution(object):

    def get_mid(self, nums):
        prev = -1
        for i in range(0, len(nums)):
            if i+1 < len(nums):
                if nums[i+1] < nums[i]:
                    return i+1


        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """



        mid = self.get_mid(nums)
        print("mid: ", nums[mid])
        
        low = 0
        high = mid-1
        print("checkpoint 1 ")
        while low<high:
            m = int((low+high)/2)

            if nums[m] == target:
                return m
            elif target > nums[m]:
                low = m-1
            else:
                high = m
        print("checkpoint 2")
        low = mid
        high = len(nums)-1
        
        while low<high:
            
            m = int((low+high)/2)
            print(low, high, m)
            time.sleep(1)
            if nums[m] == target:
                return m
            elif target > nums[m]:
                low = m+1
            else:
                high = m

        return -1



        

assert Solution().search([4,5,6,7,0,1,2], 0) == 4
assert Solution().search([4,5,6,7,0,1,2], 1) == 5
assert Solution().search([4,5,6,7,0,1,2], 4) == 0
assert Solution().search([4,5,6,7,0,1,2], 7) == 3
##assert Solution().get_mid([4,5,6,7,0,1,2]) == 4