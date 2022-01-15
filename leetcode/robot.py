class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        history = []
        for i in range(len(s)):
            start = i
            x = startPos[0]
            y = startPos[1]

            print("Details: ", start, x,y)
            count = 0
            while start < len(s):
                if s[start] == "R":
                    y = y+1
                elif s[start] == "L":
                    y = y-1
                elif s[start] == "U":
                    x = x-1
                else:
                    x = x+1
                
                if x >= n or y >= n or x < 0 or y < 0:
                    break
                count += 1
                start += 1

            history.append(count)
        return history

            


sol = Solution() 
print(sol.executeInstructions(3, [0,1], "RRDDLU"))