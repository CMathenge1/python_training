#Write a program that takes input of 2 values and adds them. 
#The program should only accept numbers and floats only or otherwise display an 
#error “invalid character entered” and take the user to re-enter the inputs 

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid character entered. Please enter numbers or floats only.")
else:
     print(num1 + num2) 

