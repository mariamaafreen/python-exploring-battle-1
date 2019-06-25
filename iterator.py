tup = ("apple", "banana", "cherry")
it = iter(tup)

print(next(it))
print(next(it))
print(next(it))

#using class

class numbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = numbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
