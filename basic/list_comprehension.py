my_list = ['Multiple of 6' if i % 6 == 0 
           else 'Multiple of 2' if i % 2 == 0 
           else 'Multiple of 3' if i % 3 == 0 
           else i for i in range(1, 20)]
print(my_list)

my_list = [10 for i in range(20)]
print(my_list)

my_list = [10]*20
print(my_list)

my_list = [i%2 for i in range(20)]
print(my_list)