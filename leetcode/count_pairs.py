class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i*j)%k == 0:
                    count += 1
        print(count)

        return count 



        

sol = Solution()
assert sol.countPairs( nums = [3,1,2,2,2,1,3], k = 2) == 4
assert sol.countPairs(nums = [1,2,3,4], k = 1) == 0