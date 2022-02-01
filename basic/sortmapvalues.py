class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for el in nums:
            if el in map:
                count = map[el]
                count += 1
                map[el] = count
            else:
                map[el] = 1
        
        #print(map)
        map = sorted(map.items(), key=lambda x: x[1], reverse=True)
        
        res = []
        for el in range(k):
            res.append(map[el][0])
            
        #print(map)
        return res
    
#         res = []
#         size = len(map)
#         print(map)
#         print(len(nums)-k+1)
#         for el in map:
#             if (map[el] >= (size-k+1)):
#                 res.append(el)
        
#         return res
        