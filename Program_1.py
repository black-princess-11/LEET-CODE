print("Hello, World!")
r=int(input("Enter a number of row you want to display in pattern: "))
que=input("Do you want to print which pattern?[1. Right angled triangle 2. Reversed right angled triangle 3. Dimond 4. Center Tringle]: ")
i=0
if que=="Right angled triangle"or que=="right angled triangle":
    for i in range(i,r+1):
        print("*"*i,)
elif que=="Reversed right angled triangle"or que=="reversed right angled triangle":
    for i in range(r,0,-1):
        print("*"*i,)
elif que=="Dimond" or que=="dimond":
    for i in range(r):
        print(" "*(r-i-1)+"*"*(2*i+1))
    for i in range(r-2,-1,-1):
        print(" "*(r-i-1)+"*"*(2*i+1))
elif que=="Center Tringle"or que=="center tringle":
    for i in range(r):
        print(" "*(r-i-1),"*"*(2*i+1))
else:
    for i in range(i,r+1):
        print("Hi!! "*i,(" "*r))