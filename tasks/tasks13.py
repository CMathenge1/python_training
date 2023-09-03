#Write a program that takes the email and password as input from a user and checks if they are equal 
#to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and
# if not print “Invalid username or password”. 
#ONLY accept 3 tries after which it notifies you that you have been blocked
email= input("Enter the email: ")
password= input("Enter the password: ")

if email=="admin@mail.com" and password=="Admin@123":
    print("Login is successful")
else:
    print("Invalid username or password")
    trials=1
    while trials<3:
        email= input("Enter the email: ")
        password= input("Enter the password: ")
        if email=="admin@mail.com" and password=="Admin@123":
            print("Login successful")
            break
        else:
            print("Invalid email or password")
            trials+=1
        if trials==3:
           print("Account blocked")
