#for element in sequence to be executed
#sequence- iterable lists strings
#the current element in the sequence is assigned to the lopp variable
#the code block is executed
#the loop continues 

#for i in range(0,15):
 # if i % 2 == 0:
 #  print(i)

#Write a for loop to print numbers from 1 to 5
#for i in range (1,6):
   #print(i)

#Sum all the elements in a list using for loop numbers=[2,3,4,5,6,7,8,9]
#numbers = [2,3,4,5,6,7,8,9]
#total = 0
#for x in numbers:
   #total+=x
#print(total)
#print("The sum of the numbers is:", total)

# x= list(range(1,90))
# res_sev=[]
# res_fiv=[]
# for i in x:
#    if i%7==0:
#       res_sev.append(i)
#    elif (i%5==0):
#      res_fiv.append(i)
#    else:
#     pass
# print(res_sev)
# print(res_fiv)

#Store only the first 10 odd numbers between 0 and 50
# odd_numbers = []
# for i in range(0,51):
#   if i%2!=0:
#     odd_numbers.append(i)
#     if len(odd_numbers)==10:
#       break
# print(odd_numbers)

count=0
for i in range (0,50):
  if i%2!=0:
   print(i)
   count+=1
   if count==0:
      break
   else:
     pass
   



  
      
    


