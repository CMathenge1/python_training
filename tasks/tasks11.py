#Write a program that takes the date of birth of a person 
#and the program outputs the age in terms of years,months,days TODAY
from datetime import datetime
today= datetime.now()
dob= input("Enter DOB (dd-mm-yyyy)")
sdob= dob.split("-")

if len(sdob)!=3 or int(sdob[0])>31 or int(sdob[1])>12 or int(sdob[2])<1900 \
    or int(sdob[2])>2023:
    print("Wrong date format")
else:
    year=today.year-int(sdob[-1])
    month=today.month-int(sdob[1])
    if month<0:
        month= month+12
        year=year-1
    day=today.day-int(sdob[0])
    if day<0:
        day=day+31
        month=month-1
    print(f"{year} year {month} month {day} day")
    
