a = 5
b = 10

# swap without temp variable 
a = a ^ b
b = a ^ b
a = a ^ b

print(a,b)