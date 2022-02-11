class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        if word1 == word2:
            return 0
        
        if word1 == "":
            return len(word2)
        
        if word2 == "":
            return len(word1)
        
        
        
        return self.get_count(word1, word2, 0,0,0)
        
        
    def get_count(self, word1, word2, index1, index2, count):
        print(word1, word2, index1, index2, count)
        if word1 == word2:
            return count
        
        if index1 >= len(word1):
            return sys.maxint
        
        if index2 >= len(word2):
            return sys.maxint
        
        # insert 
        temp_insert_word1 = word1[:index1] + word2[index2] + word1[index1:]
        insert = self.get_count(temp_insert_word1,  word2, index1+1, index2+1, count+1)
        
        # delete
        temp_word1 = word1[:index1] + word1[index1+1:]
        
        delete = self.get_count(temp_word1, word2, index1, index2, count+1)
        
        # replace
        
        #word1[index1] = word2[index2]
        word1 = word1[:index1] + word2[index2] + word1[index1+1:]
        
        replace = self.get_count(word1, word2, index1+1, index2+1, count + 1 )
        
        return min(insert, delete, replace)
    

        