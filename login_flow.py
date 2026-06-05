print("Welcome to the BLS login system.")

print("Please enter your username and password to register.")

username_reg = input("Username: ")
password_reg = input("Password: ")

if len(password_reg) < 8:
    print("Password must be at least 8 characters long. Please try again.") 
else:

    username_check = username_reg
    password_check = password_reg

    print("Thank you for registering, Your details have been saved.\nplease login to access your account.")

    username_login = input("Username: ")
    password_login = input("Password: ")

    if username_login == username_check and password_login == password_check:
        print ("Login is successful, welcome to your BLS account.")
    else:
        print("Login failed, login details did not match.")

