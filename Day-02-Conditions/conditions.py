# CS Comeback - Day 2
# Topics: Input, If, Elif, Else, Logical Operators

# Exercise 1: Age Checker
age = int(input("How old are you? "))

if age < 0:
    print("Invalid age!")
elif age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")


# Exercise 2: Grade Calculator
score = int(input("What was your score? "))

if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")


# Exercise 3: FACEIT Level Checker
faceit_level = int(input("What is your FACEIT level? "))

if faceit_level < 1 or faceit_level > 10:
    print("Invalid FACEIT level")
elif faceit_level == 10:
    print("High level")
elif faceit_level >= 7:
    print("Experienced")
elif faceit_level >= 4:
    print("Intermediate")
else:
    print("Beginner")


# Exercise 4: Login System
username = input("Enter username: ").strip()
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
elif username != "admin":
    print("Incorrect username!")
else:
    print("Incorrect password!")
