my_list = ["blue", "red", "green"]

#1- Using sort or srted directly or with specifc keys
my_list.sort() #sorts alphabetically or in an ascending order for numeric data 
print(my_list)
my_list = sorted(my_list, key=len) #sorts the list based on the length of the strings 
print(my_list)

