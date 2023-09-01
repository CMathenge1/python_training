#Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.
#prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]
prods= [['omo', '30kshs','300'], ['milk', '50kshs', '200'], ['bread','45kshs','359'], ['coffee','5kshs','79']]
total=int(prods[0][2])+int(prods[1][2])+int(prods[2][2])
print(total)