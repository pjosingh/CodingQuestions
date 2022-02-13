class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split(" ")
        string_builder = ""
        for i in range(len(words)-1, -1, -1):
            if words[i] == "":
                continue

            if string_builder == "":
                
                string_builder += words[i]
            else:
                string_builder = string_builder + " " + words[i]
                    
            
        print(string_builder)
        return string_builder



sol = Solution()
assert sol.reverseWords("the sky is blue") == "blue is sky the"
assert sol.reverseWords("  hello world  ") == "world hello"
assert sol.reverseWords("a good   example") == "example good a"
