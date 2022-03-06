import time 

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        mapping = {}
        for el in candidates:
            mapping[el] = True
        res = []
        self.__utility(sorted(mapping), target, 0, [], res)
        r = {}
        rr = []
        for el in res:
            t = tuple(sorted(el))
            if t not in r:
                
                rr.append(el)
                    
            r[t] = True

        return rr
    
    def __utility(self, mapping, target, current, current_trail, res):
        #time.sleep(1)

        if current == target:
            res.append(current_trail)
            return
        
        if current > target:
            return

        for el in mapping:
            if current + el == target:
                res.append(current_trail+[el])
            elif current + el < target:
                self.__utility(mapping, target, current+el, current_trail + [el], res) 
            else:
                break
        
      
