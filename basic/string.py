a="hello world"

print(a[0:3]) # hel
print(a[0:4]) # hell
print(a[6:]) # world
print(a[:]) # hello world
print(a[-1]) # d
print(a[:-1]) # hello worl

# remove a characte at index i 
index = 4
print(a[index])
print(a[:index]+a[index+1:])
