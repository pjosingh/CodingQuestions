import time 


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        

        # find mid

        mid = self.find_middle(nums)

        # search in first part 

        res = self.search_util(nums, 0, mid-1, target)
        if res == -1:
            res = self.search_util(nums, mid, len(nums)-1, target)

        return res

    def search_util(self, nums, low, high, target):
        
        while (low<=high):
            mid = int((low+high)/2)

            if target < nums[mid]:
                high = mid - 1
            elif target == nums[mid]:
                return mid
            else:
                low = mid+1
        return -1


    
    def find_middle(self, nums):

        
        low = 0
        high = len(nums)-1

        if (nums[low] < nums[high]):
            return low
        
        while (low<high):
            mid = int((low+high)/2)
            #print(f' mid: {mid} low: {low} high: {high}   Nums: {nums}')
            #time.sleep(1)
            if (mid != low and nums[mid] <= nums[low]):
                high = mid+1
                if (nums[mid]<=nums[mid-1]):
                    return mid
            else:
                if (nums[mid+1]<nums[mid]):
                    return mid+1
                low = mid

        return low


assert Solution().find_middle([3,1]) == 1
assert Solution().search([3,1],0) == -1

assert Solution().search(nums = [0,1,2,4,5,6,7], target = 0) == 0
assert Solution().find_middle([4,5,6,7,0]) == 4        
assert Solution().find_middle([4,5,6,7,0,1,2]) == 4
assert Solution().search(nums = [4,5,6,7,0,1,2], target = 0) == 4
assert Solution().search(nums = [4,5,6,7,0,1,2], target = 3) == -1
assert Solution().search(nums = [4,5,6,7,0], target = 7) == 3
assert Solution().search(nums = [4,5,6,7,0], target = 4) == 0
