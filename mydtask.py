my_ds = [23, "Jane" ,(560), [ "Lesson", "Maths" ,{"currency" :"KES"}], 987, (76, "John")]

#print KES
print(my_ds[3][2]["currency"])
#print 560
print(my_ds[2])
#print maths
print(my_ds[3][1])
#add amount:90 to dictionary
my_ds[3][2]["amount"]=90
print(my_ds)
#change 987 to 789 using inbuilt method

a= str(987)
reversed= a[::-1]
print(reversed)





