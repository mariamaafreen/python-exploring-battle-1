class Parent:
    parentname = ""
    childname = ""
 
    def show_parent(self):
        print(self.parentname)
 
 
class Child(Parent):
    def show_child(self):
        print(self.childname)
 
 
c = Child()  
c.parentname = "fathima"   
c.childname = "sanu"
c.show_parent()   
c.show_child()    