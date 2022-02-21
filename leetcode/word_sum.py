class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """

        map = {}
        map['a'] = 0
        map['b'] = 1
        map['c'] = 2
        map['d'] = 3
        map['e'] = 4
        map['f'] = 5
        map['g'] = 6
        map['h'] = 7
        map['i'] = 8
        map['j'] = 9
        

        rev = {}
        rev[0] = 'a'
        rev[1] = 'b'
        rev[2] = 'c'
        rev[3] = 'd'
        rev[4] = 'e'
        rev[5] = 'f'
        rev[6] = 'g'
        rev[7] = 'h'
        rev[8] = 'i'
        rev[9] = 'j'
        

        firstSum = self.get_sum(map, firstWord)

        secondSum = self.get_sum(map, secondWord)
        
        targetSum = self.get_sum(map, targetWord)

        # digits = self.get_digits(firstSum+secondSum)
        # word = ""
        # for el in digits:
        #     word = word + rev[el]

        #print(word, digits, firstSum, secondSum)
        #return word[::-1] == targetWord
        return targetSum == (firstSum+secondSum)
    
    def get_sum(self, map, firstWord):
        firstSum = 0
        mul = 1
        for el in range(len(firstWord)-1, -1,-1):
            # 0*1 + map[b] = 1
            # 1*10 + map[c] = 10 + 2 = 12
            # 
            firstSum = firstSum + map[firstWord[el]]*mul
            mul = mul*10
        return firstSum


    def get_digits(self, target):
        queue = []
        while target != 0:
            queue.append(int(target%10))
            target = int(target/10)
        return queue





        

sol = Solution()

'''
acb - 021
cba - 210
sum - 231 - cdb
'''
assert sol.isSumEqual("acb", "cba", "cdb") == True
assert sol.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aab") == False
assert sol.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aaaa") == True
