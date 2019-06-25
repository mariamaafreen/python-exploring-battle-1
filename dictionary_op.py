#creating a dictionary

my_dict = {'name':'Jack', 'age': 26}


print(my_dict['name'])
print(my_dict.get('age'))

# changing or adding elements in dictionary

my_dict['age'] = 27

print(my_dict)


my_dict['address'] = 'Downtown'  

print(my_dict)

#deleting elements from dictionary

squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

print(squares.pop(3))  
print(squares)


print(squares.popitem())
print(squares)


del squares[2]  
print(squares)


squares.clear()
print(squares)



