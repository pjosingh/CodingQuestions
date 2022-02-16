from __future__ import division


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        mapping = {} 
        for el in nums:
            res = self.divide(el)
            if res[0] in mapping:
                mapping[res[0]].append(el)
            else:
                adj = []
                adj.append(el)
                mapping[res[0]] = adj
        
        print(mapping)
        # form number
        response = ""
        
        for i in range(9,-1,-1):
            if i in mapping:
                if len(mapping[i]) == 1:
                    response += str(mapping[i][0])
                else:
                    number = self.largestNumber(mapping[i])
                    response += number

        print(response)
        return response

    
    def divide(self, el):
        res = []
        while el != 0:
            digit = el%10
            res.append(int(digit))
            el = int(el/10)
        return res[::-1]


sol = Solution()
assert sol.largestNumber([10,2]) == "210"
assert sol.largestNumber([3,30,34,5,9]) == "9534330"