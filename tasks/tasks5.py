#Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. 
#Return the largest of the three. Do this without using the the inbuilt max () function!
num1= int(input("Enter num1: "))
num2= int(input("Enter num2: "))
num3= int(input("Enter num3: "))
if num1>num2 and num1>num3:
    print("num1 is the largest")
elif num2>num3 and num2>num1:
    print("num2 is the largest")
else:
    print("num3 is the largest")