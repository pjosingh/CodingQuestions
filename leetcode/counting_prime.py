from math import sqrt
 

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        for i in range (n):
            if self.isPrime(i):
                count += 1        

        return count

    
    def isPrime(self, n):
    
        # Corner case
        if (n <= 1):
            return False
    
        # Check from 2 to sqrt(n)
        for i in range(2, int(sqrt(n))+1):
            if (n % i == 0):
                return False
    
        return True
sol = Solution()
print(sol.countPrimes(10))
        