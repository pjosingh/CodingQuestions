class Solution(object):

    def minDistance(self, word1, word2):
        return self.editDistance(word1, word2, len(word1), len(word2))
        
    def editDistance(self, str1, str2, m, n, d = {}):
        print(d)
        key = m, n
    
        # If first string is empty, the only option
        # is to insert all characters of second
        # string into first
        if m == 0:
            return n
    
        # If second string is empty, the only
        # option is to remove all characters
        # of first string
        if n == 0:
            return m
    
        if key in d:
            return d[key]
            
        # If last characters of two strings are same,
        # nothing much to do. Ignore last characters
        # and get count for remaining strings.
        if str1[m - 1] == str2[n - 1]:
            return self.editDistance(str1, str2, m - 1, n - 1)
    
        # If last characters are not same, consider
        # all three operations on last character of
        # first string, recursively compute minimum
        # cost for all three operations and take
        # minimum of three values.
        
        # Store the returned value at dp[m-1][n-1]
        # considering 1-based indexing
        
        d[key] = 1 + min(self.editDistance(str1, str2, m, n - 1), # Insert
                        self.editDistance(str1, str2, m - 1, n), # Remove
                        self.editDistance(str1, str2, m - 1, n - 1)) # Replace
        return d[key]

sol = Solution()
#print(sol.minDistance("horse","ros"))

print(sol.minDistance("intention", "execution"))
