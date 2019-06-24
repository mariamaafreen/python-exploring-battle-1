from functools import reduce

my_list = [5, 8, 10, 20, 50, 100] 
product = reduce((lambda x, y: x * y),my_list)

print (product) 

sum = reduce((lambda x, y: x + y),my_list)

print(sum)
