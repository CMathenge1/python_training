person= { "name":"Ken", "age":30, "phone":2345}

print(person["name"])
print(person.get("age"))
print(person.keys())
person["amount"]=90
print(person)
#print(person.pop("phone"))
print(person.popitem())
