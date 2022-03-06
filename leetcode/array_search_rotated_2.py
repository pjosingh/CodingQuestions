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
        print(f'mid: {mid}')

        # adjust ends
        temp = mid
        while mid-1 >=0 and nums[mid-1] == nums[mid]:
            mid = mid-1
        while temp+1 <len(nums) and nums[temp] == nums[temp+1]:
            temp = temp+1
        high = temp

        print(f'new mid: {mid}, end : {high}')

        # search in first part 

        res = self.search_util(nums, 0, mid-1, target)

        if res == -1:
            res = self.search_util(nums, high, len(nums)-1, target)

        if res == -1:
            return False
        else:
            return True

    def search_util(self, nums, low, high, target):
        print(f'search : {nums}, {low}, {high}')
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
            if (mid != low and nums[mid] <= nums[low]):
                high = mid+1
                if (nums[mid]<=nums[mid-1]):
                    return mid
            else:
                if (nums[mid+1]<=nums[mid]):
                    return mid+1
                low = mid


assert Solution().search([1,2,2,2,0], 0) == True

assert Solution().search(nums=[1,1], target=0) == False


assert Solution().search(nums = [2,5,6,0,0,1,2], target = 0) == True
assert Solution().search(nums = [2,5,6,0,0,1,2], target = 2) == True
assert Solution().search(nums = [2,5,6,0,0,1,2], target = 1) == True
assert Solution().search(nums = [2,5,6,0,0,1,2], target = 6) == True
assert Solution().search(nums = [2,5,6,0,0,1,2], target = 3) == False

# assert Solution().find_middle([3,1]) == 1
# assert Solution().search([3,1],0) == -1

# assert Solution().search(nums = [0,1,2,4,5,6,7], target = 0) == 0
# assert Solution().find_middle([4,5,6,7,0]) == 4        
# assert Solution().find_middle([4,5,6,7,0,1,2]) == 4
# assert Solution().search(nums = [4,5,6,7,0,1,2], target = 0) == 4
# assert Solution().search(nums = [4,5,6,7,0,1,2], target = 3) == -1
# assert Solution().search(nums = [4,5,6,7,0], target = 7) == 3
# assert Solution().search(nums = [4,5,6,7,0], target = 4) == 0
