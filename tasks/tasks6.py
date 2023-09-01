#Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. 
#If the password is correct access is granted. After you show them a message , the account is blocked
password= "admin@123"
attempts= 4
for attempts in range(1, attempts+1):
    mypas= input("Enter password: ")

    if mypas==password:
        print("Access granted")
        break
    if mypas!=password and (attempts>0 and attempts<=4):
        print ("Wrong password, try again")
        if attempts==4:
          print("Account is blocked")
    else:
        pass



