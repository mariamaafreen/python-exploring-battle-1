#creating a set

set_ = {"a", "b", "c"}
print(set_)

#acessing items 

print("b" in set_)

#add items

set_.add("d")
set_.add("e")

print(set_)

set_.update("1","2","3")
print(set_)

#length of a set

print(len(set_))

#remove items

set_.remove("b")
print(set_)

set_.discard("1")
print(set_)

x = set_.pop()
print(x)
print(set_)

set_.clear()
print(set_)