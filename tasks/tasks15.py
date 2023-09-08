#Write a program that takes input of someone's basic salary and benefits, adds them to 
#find the gross salary then uses  the gross salary to find the NHIF
basic_salary= float(input("Enter the basic salary: "))
benefits= float(input("Enter the benefits: "))
gross_salary= basic_salary+benefits

if gross_salary<=5999:
    NHIF_contribution=150
elif gross_salary>=6000 and gross_salary<=7999:
    NHIF_contribution=300
elif gross_salary>=8000 and gross_salary<=11999:
    NHIF_contribution=400
elif gross_salary>=12000 and gross_salary<=14999:
    NHIF_contribution=500
elif gross_salary>=15000 and gross_salary<=19999:
    NHIF_contribution=600
elif gross_salary>=20000 and gross_salary<=24999:
    NHIF_contribution=750
elif gross_salary>=25000 and gross_salary<=29999:
    NHIF_contribution=850
elif gross_salary>=30000 and gross_salary<=34999:
    NHIF_contribution=900
elif gross_salary>=35000 and gross_salary<=39999:
    NHIF_contribution=950
elif gross_salary>=40000 and gross_salary<=44999:
    NHIF_contribution=1000
elif gross_salary>=45000 and gross_salary<=49999:
    NHIF_contribution=1100
elif gross_salary>=50000 and gross_salary<=59999:
    NHIF_contribution=1200
elif gross_salary>=60000 and gross_salary<=69999:
    NHIF_contribution=1300
elif gross_salary>=70000 and gross_salary<=79999:
    NHIF_contribution=1400
elif gross_salary>=80000 and gross_salary<=89999:
    NHIF_contribution=1500
elif gross_salary>=90000 and gross_salary<=99999:
    NHIF_contribution=1600
else:
    gross_salary>=100000
    NHIF_contribution=1700

print("The gross salary is:", gross_salary)
print("NHIF is:", NHIF_contribution)
#NSSF contribution
if gross_salary<=18000:
    NSSF= gross_salary * 0.06
else:
    NSSF=18000*0.06
print(NSSF)

#calculate an individual’s NHDF
NHDF = gross_salary *  0.015
print("nhdf is:", NHDF)
#calculate the taxable income
taxable_income= gross_salary-(NSSF+NHDF)
#calculate payee from the taxable income
personal_relief=2400

if taxable_income<=24000:
    payee= 24000 * 0.1
    net_payee=payee-personal_relief
elif taxable_income>24000 and taxable_income<=32333:
    payee= (taxable_income-24000)*0.25+2400
    net_payee=payee-personal_relief
elif taxable_income>32333 and taxable_income<=500000:
    payee=(taxable_income-32333)*0.3+4483.25
    net_payee=payee-personal_relief
elif taxable_income>500000 and taxable_income<=800000:
    payee=(taxable_income-500000)*0.325+144783.35

else:
    taxable_income>800000
    payee= (taxable_income*0.35)+ 242283.35
    net_payee=payee-personal_relief

print("PAYEE is:", net_payee)

# Calculate the net salary
net_salary = gross_salary - (NHIF_contribution + NHDF +  NSSF + net_payee)
print("Net salary is:",net_salary)