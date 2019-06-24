number = int(input("enter a number"))

fact = 1

if(number==0):
    print("the factorial is 0")
elif(number==1):
    print("the factorial is 1")

else:
    for i in range(1,number+1):
         fact = fact * i
    print("the factorial of %d is %d" %(number,fact))
         