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
    price=(units * 20)
elif (units>50 and units<=100):
    price=((units-50)* 40)+1000
else: 
    (units>100)
    price=((units-100)*100)+3000
print(price)

