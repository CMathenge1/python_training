#conditional statements (if, else statements,)
#Write a program to check whether a person can vote or note
 
age =10
if (age>=18):
   print("You can vote")
else:
   print("You can't vote")

average_marks= 90
if average_marks  >= 70:
 		 print("A")
elif average_marks  >= 60 and average_marks  < 70:
 	 print("B")
elif average_marks  >= 50 and average_marks  < 60:
   		print("C")
elif average_marks  >= 40 and average_marks  < 50:
   		print("D")
else:
   print("E")


num1= int(input("Enter number1: "))
num2= int(input("Enter number2: "))
num3= int(input("Enter number3: "))
if (num1>num2 and num1>num3):
	print("Largest number is", num1) 
elif (num2>num1 and num2>num3):
     print("Largest number is", num2)
else:
	print("Largest number is", num3)



