file1 = open("file1.txt","w") 
L = ["This is chennai \n","it is an awesome place \n","it has many famous places to visit \n"]  
  

file1.write("Hello \n") 
file1.writelines(L) 
file1.close() 
  
file1 = open("file1.txt","r+")  
  
print ("Output of Read function is ")
print (file1.read()) 

  

file1.seek(1)  
  
print ("Output of Readline function is ")
print (file1.readline()) 

  
file1.seek(0) 
  

print ("Output of Read(9) function is ")
print (file1.read(9)) 

  
file1.seek(0) 
  
print ("Output of Readline(9) function is ")
print (file1.readline(9)) 
  
file1.seek(0) 

print ("Output of Readlines function is ")
print (file1.readlines()) 

file1.close() 
