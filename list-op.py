# Adding elements in a list

l = []

for i in range(1,4):
    l.append(i)

print(l)

l.insert(0,0)
print(l)

l.extend([4,5,6])
print(l)

#Acessing elements

print(l[3])
print(l[0])

print(l[-1])
print(l[-6])

#Removing elements

l.remove(3)
print(l)

l.pop()
print(l)

l.pop(3)
print(l)

#slicing of a list
Sliced_List = l[3:8] 
print(Sliced_List) 
  
sliced_list = l[-1:3]
print(sliced_list)

#sum()

print(sum(l))

#min()

print(min(l))

#max()

print(max(l))

#len()

print(len(l))

#count()

print(l.count(2))

#index

print(l.index(1))

