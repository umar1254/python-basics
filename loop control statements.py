#loop control statements

fruits = ["apple", "banana", "cherry", "date"]


for fruit in fruits:
        if fruit == "cherry":
            break    #exit the loop
for fruit in fruits:
    if fruit == "cherry":
        continue  #skips cherry and goes to the other iteration
for fruit in fruits:
    if fruit == "cherry":
        pass #placeholder, no action is needed
    print(fruit)
    
    
    
    
    
    
count = 0
    
while count < 5:
        print (count)
        count += 1
        if count ==3:
            break  #exits loop when count is reached