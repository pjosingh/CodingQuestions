m = "leetcode"
dic = [0]*26
for el in m:
    dic[ord(el)-ord('a')] += 1

print(dic)
