class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = self.convert(s)
        t = self.convert(t)
        return s == t

        
    def convert(self, s):
        queue = []

        for el in s:
            if el == '#':
                if queue:
                    queue.pop()
            else:
                queue.append(el)
        
        return str(queue)


        

sol = Solution()

assert sol.backspaceCompare( s = "ab#c", t = "ad#c") == True
assert sol.backspaceCompare(s = "ab##", t = "c#d#") == True
assert sol.backspaceCompare(s = "a#c", t = "b") == False
assert sol.backspaceCompare("a##c", "#a#c") == True

