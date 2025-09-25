#control statements

num = 10

if num > 0:
    print("this number is positive")
    
    #this number is positive will appear in the screen
    
if num > 0:
    print("this number is positive")
else:
    print("this number is equal to or less tean zero")
    
    #this will reslut in this number is equal to or less tean zero appearing on screen
    
    
    
    #control statements part 2
    
    num1 = int(input("enter the first number:"))
    num2 = int(input("enter the second number:"))
    
    if num1 > num2:
        print(num1, "is greater than", num2)
    elif num2 > num1:
        print(num2, "is greater than", num1)
    else:
        print("both numbers are equal")