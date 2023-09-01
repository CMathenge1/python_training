#Write a program which accepts email as form input or from terminal. 
#Validate the email by checking if it's a valid email
email=input("Enter email: ")
if len(email.strip())>6 and (email.index("@")>2) and (email.index(".")-email.index("@"))>3 and email.index(".")>-2:
    print("Valid Email")
else:
    print("Not valid")
