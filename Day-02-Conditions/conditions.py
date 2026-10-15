# CS Comeback - Day 2
# User Input and Conditions

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
elif username != "admin":
    print("Username is incorrect!")
else:
    print("Password is incorrect!")
