#control statements part 2
    
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
    
if num1 > num2:
    print(num1, "is greater than" , num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("both numbers are equal")
    
    #users will be promted to input two numbers, one after the other .the screen will then display which number is greater