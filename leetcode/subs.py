class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = 0

        for el in s:
            flag = False

            for j in range(index, len(t)):
                if t[j] == el:
                    flag = True
                    index = j+1
                    break
            #print(el, flag)
            if flag == False:
                return False
            
        return True
            
            


sol = Solution()

assert sol.isSubsequence(s = "abc", t = "ahbgdc") == True
assert sol.isSubsequence(s = "axc", t = "ahbgdc") == False
assert sol.isSubsequence("acb", "ahbgdc") == False
print("=====")
assert sol.isSubsequence("aaaaaa", "bbaaaa") == False