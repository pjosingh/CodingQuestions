class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        fwd_list = []
        rev_list = []


        # 5,2,3,4
        # [24,60,40,30]
        # fwd = 5, 10, 30, 120
        # bck = 4, 12, 24, 120
        # rev = 120, 24, 12, 4
        # res = 24, 5 * 12, 10*4, 30
        # res= 24, 60, 40, 30

        fwd = 1
        for el in nums:
            fwd = fwd*el
            fwd_list.append(fwd)
        rev = 1
        for el in range(len(nums)-1, -1, -1):
            rev = rev*nums[el]
            rev_list.append(rev)
        rev_list.reverse()

        for el in range(len(nums)):
            if el == 0:
                res.append(rev_list[el+1])
            elif el == len(nums)-1:
                res.append(fwd_list[el-1])
            else:
                res.append(rev_list[el+1]*fwd_list[el-1])


        return res


sol = Solution()
print(sol.productExceptSelf([5,2,3,4]))
[-1,1,0,-3,3]
print(sol.productExceptSelf([1,2]))