from functools import cache


class Solution(object):
    def wordBreak(self, s, wordDict):
        global c
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if s == "":
            return True
        c = {}
        map = {}
        for word in wordDict:
            map[word] = True

        return self.util(str(reversed(s)), map)

    c = {}

    def util(self, s, map):
        global c
        print(c, map, s)
        if s in c:
            return c[s]

        if s == "":
            return True
        word = ""
        for i in range(len(s)):
            # i =0

            word += s[i] # s[0] = a
            if word in map: # true
                if self.wordBreak(s[i+1:], map):
                    return True
        
        c[s] = False
        return False
        


sol = Solution()
# assert sol.wordBreak(s = "leetcode", wordDict = ["leet","code"]) == True
# assert sol.wordBreak(s = "amazonkindle", wordDict = ["ama","zon", "amazon", "kindle", "kind"]) == True
assert sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) == False




