days = {"Monday", "Tuesday", " Wednesday", "Thursday", "Friday", "Saturday", "sunday", "sunday","sunday", "sunday"}
print(days)
#remove friday and sunday
days.remove("Friday")
days.remove("sunday")
print(days)
days.add("Friday")
days.add("sunday")
print(days)
days.discard("Friday")
print(days)