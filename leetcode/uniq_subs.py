

class Solution(object):
    max_val = 0

    def maxLength(self, arr):
        global max_val
        max_val = 0


        if len(arr) == 1:
            return len(arr)
        

        for i in range(len(arr)):
            
            for j in range(i+1, len(arr)):
                l = len(str(set(arr[i]).intersection(arr[j])))
                if l > max_val:
                    max_val = l
        print('max', max_val)
        return max_val

            




sol = Solution()

assert sol.maxLength(["un","iq","ue"]) == 4
assert sol.maxLength(["cha","r","act","ers"]) == 6
assert sol.maxLength(["abcdefghijklmnopqrstuvwxyz"]) == 26
assert sol.maxLength(["aa","bb"]) == 0
