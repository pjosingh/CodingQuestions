class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        mul = 1
        res = []
        temp = n
        while temp != 0:
            res.append(mul)
            if (mul > 0):
                mul = -mul
            else:
                mul = -mul
                mul += 1
            temp = temp -1

        if n%2 != 0:
            res = res[:-1]
            res.append(0)
        return res





sol = Solution()
print(sol.sumZero(5))
print(sol.sumZero(3))
print(sol.sumZero(1))
print(sol.sumZero(4))