class Solution(object):
    def generateParenthesis(self, n):
        print("input: ", n)

        
        
        res= []
        stack = []

        self.gen(stack, res, n, "")
        return res

    def gen(self, stack, res, n, current):

        if n == 0:
            while len(stack)>0:
                stack.pop()
                current += ")"
            res.append(current)
            return



        # expected answer for n = 2
        # ["(())","()()"]
        # sudo algorithm 
        # if n != 0, either put to current list n put on stack for closing it  or if there is a element on stack, pop it. 
        # if n == 0, if stack is empty, put on response list. if not, empty the stack, put on response list. 

        copy = current[:]
        copy = copy + "("
        stack_copy = stack[:]
        stack_copy.append(")")

        if stack:
            el = stack.pop()
            current = current+el
            self.gen(stack, res, n, current)    

        self.gen(stack_copy, res, n-1, copy)
        


        


sol = Solution()
print(sol.generateParenthesis(1))
print(sol.generateParenthesis(3))