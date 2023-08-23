mylist=[]
car_brands=["Ford", "Nissan", "Audi", "BMW", "Toyota", "banana", "oranges"]
#print(car_brands[1])
#print(car_brands[-2])

#Range of indexes
#start:end
#print(car_brands[1:4])
#print(car_brands[4:6])
#print(car_brands[:5])
#print(car_brands[5:])
#negative indexing
#print(car_brands[-4:])
#Create a List of days of the week. Print the day today using an index
#days= ["Moanday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#print(days[1])

#List methods; Access Items, change, and add items
#append method
#cars= ["Volvo", "Audi"]
#cars.append("Ford")
# adding list to list using .__add__, then assigning value to it.
#print(cars)
#cars.insert(1,"Ford")
#print(cars)
car=["Volvo", "Ford",["Toyota", "Mercedes", ["Mazda", "Subaru"]], "Audi"]
#insert Nissan between Mazda and Subaru
#car[2][2].insert(1, "Nissan")
#print(car)
#extend model
model= ["SUV", "Minivan", "Van"]
#car.extend(model)
#print(car)
owners= ["Allan", "Ken", "Ivy"]
#car.extend(model), car.extend(owners)
#print(car)
#car= car+ model + owners
#print(car)

#removing an item from a list
#car.remove("Ford")
#print(car)
#pop- 
#car.pop()
#print(car)
#del()-
#del car 
#print(car)
#car.clear()
#print(car)

#del car[1]
#print(car)
#prompt a user to input a list of cars. Input 3 cars, Initialize and empty list

car1= input("Enter car name:")
car2= input("Eneter car name:")
car3= input("Eneter car name:")
models=[]
models.append(car1)
models.append(car2)
models.append(car3)
print(models)
del models[1]
print(models)

models.pop(0)
print(models)

models.clear()
print(models)

del models
print(models)


