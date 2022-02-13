class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        word = ""
        if s == "":
            return True

        for i in range(len(s)):
            word += s[i]
            if word in wordDict:
                if self.wordBreak(s[i+1:], wordDict):
                    return True
            
        return False

        


sol = Solution()
assert sol.wordBreak(s = "leetcode", wordDict = ["leet","code"]) == True
assert sol.wordBreak(s = "amazonkindle", wordDict = ["ama","zon", "amazon", "kindle", "kind"]) == True
assert sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) == True

