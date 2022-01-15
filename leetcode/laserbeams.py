class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """

        history = []
        for row in bank:
            count = 0
            for el in range(len(row)):
                if (row[el] == "1"):
                    count += 1
            #print("Count: ", count)
            history.append(count)
        
        sum = 0
        prev = 0
        current = 0
        for el in history:
            if el == 0:
                continue
            
            current = el
            if prev != 0:
                if current != 0:
                    sum += prev * current

            prev = current

        return sum

sol = Solution()
print(sol.numberOfBeams(["011001","000000","010100","001000"]))
print(sol.numberOfBeams(["000","111","000"]))