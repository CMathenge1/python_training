# x=0
# def myincrement():
#     x= x+1
#     return(x)
    
# x= myincrement()
# print("X1 is", x)
#classes are a collection of functions and variables that are related and can manipulate each other.
#a function inside a class is called a method.
#A variable inside a class are called properties
#Representation of somthing real e.g student class
#here all functions and properties are related to a student e.g create_student(), email

class Calculator():
     x=0
     def myincrement(self):
        self.x= self.x+1


class Person():
    name= ""
    gender= ""
    email= ""
    phone= ""
    details= []

    #Constructor- a special method used to instantiate initial values
    def __init__(self,n,g,e,p):
        self.name= n
        self.gender= g
        self.email= e
        self.phone= p
        self.add()
    def add (self):
        self.details.append(self.name)
        self.details.append(self.gender)
        self.details.append(self.email)
        self.details.append(self.phone)

# p1=Person("John", "Male", "j@mail.com", 254702345876)
# print(p1.phone)
# print(type(p1))
# p1.add()
# print(p1.details)

# p1= Person(input("Enter Name:"), 
#            input("Enter Gender:"),
#            input("Enter Email:"),
#            input("Enter Phone:"))
# print(p1.details)

p1= Person()
print(p1.details)