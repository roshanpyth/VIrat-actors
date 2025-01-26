login={
    "username1":"password1",
    "username2":"password2",
    "username3":"password3"
    
}


username=input("Please enter your username  ")

if username not in login:
     print(" You are not a user ")
else:
    password=input("Please enter your password  ")
    if password==login[username]:
         print("You have succesfully logged in, welcome back")
    else:
        print("Password is wrong")