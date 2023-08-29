#write a programto check whether a number is divisible by 7
#write a program to calculate electricity bill based on the following criteria. 
#unit: first 50 units Kshs.20, Next 50 units Kshs.40, After 100 units Kshs 100
n= int(input("Enter a number: "))
if (n%7 == 0):
    print(n, "is divisible by 7. " )
else:
    print(n, "is not divisible by 7. ")


units= int(input("Enter a number: "))
if (units<=50):
    print("The electricity bill is", 20)
elif (units<=100):
    print("The electricity bill is", 40)
else:
    print("The electricity bill is", 100)

