#https://builtin.com/data-science/python-code-snippets
str1 = "hello"
str2 = "😀"

def str_size(s):
  return len(s.encode('utf-8'))

print(str1.encode('utf-8'))
print(str_size(str1))
print(str2.encode('utf-8'))
print(str_size(str2))

