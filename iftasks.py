#Given a variable temperature with a value of 25°C, 
#write an if statement to check if the temperature is above 30°C using the greater than (>) operator
temperature = 25
if (temperature>30):
    print("Temperature is above 30°C")
else:
    print("Temperature is below 30°C")


#Create a dictionary called stock with items as keys and their quantities as values. 
# Write an if-else statement to check if the quantity of "apples" is zero using the equality (==) operator.

stock={"Bananas":30, "Apples":4, "Grapes":12}
if (stock["Apples"]==0):
    print("Apple is equal to zero")
else:
    print("Apples are not equal to zero")

#Declare a list called even_numbers containing integers. 
# Write an if statement to check if the first element of the list is an even number using the modulo (%) operator
even_number=[1,2,3]
if (even_number[0]%2==0):
    print("Even number")
else:
    print("Not an Even number")

#Imagine you have a list employees containing dictionaries with keys "name", "hours_worked", and "hourly_rate". 
# Write a code snippet using if statements to calculate the salary for
#  an employee named "Alice" based on her hours worked and hourly rate.
list_employees=[{"Name":"Alice", "Hours_worked":8, "Hourly_rate":250}]

if(list_employees[0]["Name"]=="Alice"):
    print(True)
else:
    print(False)

salary= (list_employees[0]["Hours_worked"])*(list_employees[0]["Hourly_rate"])
print(salary)


#Create a dictionary book_ratings with book titles as keys and their ratings as values. 
# Write an if-elif-else statement to find out if a book "The Adventure" has a rating of 5 or is rated below 2
book_ratings= {"Titles": "The Adventure", "rating":3}
if(book_ratings["rating"]==5):
    print("rate is 5")
elif (book_ratings["rating"]<5) and (book_ratings["rating"]>=2):
    print("rate above 2 but below 5")
else:
    (book_ratings["rating"]<2)
    print("rate is below 2")

#Suppose you have two sets: set_x and set_y. Write a code snippet using conditional statements to check 
#if the symmetric difference between the two sets is not empty, using the ^ (symmetric difference) operator

set_x= {"Monday", "Tuesday", "Wednesday",3}
set_y= {"one", "two", "three",3}
set= set_x.symmetric_difference(set_y)
print(set)
if len(set)==0:
    print("empty")
else:
 print("not empty")
