test="prabhjot"
print(test)

s="loveleetcode"
letters='abcdefghijklmnopqrstuvwxyz'
index=[s.index(l) for l in letters if s.count(l) == 1]
print(index)
print(min(index) if len(index) > 0 else -1)