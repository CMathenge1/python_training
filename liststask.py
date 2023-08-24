trainees= ["John", [2,["James", "Mary"]]]
#display 2
print(trainees[1][0])
#output James
print(trainees[1][1][0])
#add 56
trainees.append(56)
print(trainees)
#add Mike between James and Mary
trainees[1][1].insert(1, "Mike")
print(trainees)
#change value of 2 to 8
trainees[1][0]=8
print(trainees)
#remove John and Mary
del trainees[1][1][2]
del trainees[0]
print(trainees)
print(len(trainees))