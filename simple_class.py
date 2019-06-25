class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myname(self):
    print("Hello my name is " + self.name)

  def myage(self):
    print("my age is %d" % self.age)    

p1 = Person("sanu", 19)
p1.myname()
p1.myage()
