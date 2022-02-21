class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = self.get_digits(num)
        '''
        03, 12
        02, 13
        032, 1
        0, 231

        '''
        
        return self.generate(digits)

    def generate(self, digits):
        digits.sort()
        print(digits)
        i,j = len(digits)-1,len(digits)-2

        first, second = 0,0

        mul = 1
        while j>=0:
            print(digits[i], digits[j])
            first += digits[i]*mul
            second += digits[j]*mul
            i = i-2
            j = j-2
            mul = mul*10
        
        print(first, second)
        return first+second

    def get_digits(self, num):
        queue = []

        while num != 0:
            queue.append(int(num%10))
            num = int(num/10)
        return queue
    
    

# Unit tests
sol = Solution()
assert sol.minimumSum(2932) == 52
assert sol.minimumSum(4009) == 13
assert sol.minimumSum(9999) == 198

#assert sol.get_digits(4009) == [9,0,0,4]
#assert sol.generate([9,0,0,4]) == 13

