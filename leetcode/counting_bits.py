
class Solution:
    def countBits(self, n: int):
        
        res = []
        for i in range(n+1):
            res.append(self.count(i))
            
        #print(f' response: {res}')            
        return res
    
    def count(self, target):

        c = 0
        while target:
            if target%2 == 1:
                c += 1
            target = int(target/2)
        return c

assert Solution().countBits(2) == [0,1,1]
assert Solution().countBits(5) == [0,1,1,2,1,2]