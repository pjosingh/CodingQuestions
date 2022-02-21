class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        stack1 = []
        for el in a:
            stack1.append(el)
        stack2 = []
        for el in b:
            stack2.append(el)
        
        carry = 0
        response = ""
        
        while len(stack1)>0 or len(stack2) >0:
            
            current = 0
            el = self.get_element(stack1)
            if el != -1:
                current += el
            el = self.get_element(stack2)
            if el != -1:
                current += el
            
            current += carry

            if current == 2:
                carry = 1
                current = 0
            elif current == 3:
                carry = 1
                current = 1
            elif current == 1:
                carry = 0
                current = 1
            else:
                carry = 0
                current = 0
            response = str(current)+response
            
        if carry != 0:
            response = str(carry)+response
        
        return response


                
    def get_element(self, stack):
        if len(stack) > 0:
            el = stack.pop()
            if el == '1':
                return 1
            else:
                return 0
        else:
            return -1
        

        
sol = Solution()
assert sol.addBinary(a = "11", b = "1") == "100"
assert sol.addBinary(a = "1010", b = "1011") == "10101"