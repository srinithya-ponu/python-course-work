email,pwd = 'xyz@gmail.com', 'xyz@123'
max_attempts= 3

while max_attempts>0:
    useremail=input("Enter the email: ")
    password=input("Enter the password: ")
    if useremail==email and pwd==password:
        print("Login Successful")
        break
    else:
        print("Invaild Login")
    max_attempts-=1
else:
    print("Try after some time.")


#Enter the email: dj
#Enter the password: kbdjs      #Invaild Login
#Enter the email: kafjd
#Enter the password: akbdjf     #Invaild Login
#Enter the email: akdf
#Enter the password: akhdfj     #Invaild Login
#Try after some time.

#Enter the email: xyz@gmail.com
#Enter the password: xyz@123     #Login Successful
