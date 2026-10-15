# CS Comeback - Day 3
# While Loops and For Loops

# Example 1: For loop
for number in range(1, 6):
    print("Number:", number)

# Example 2: While loop
count = 1

while count <= 5:
    print("Count:", count)
    count += 1

# Example 3: Login with limited attempts
correct_password = "1234"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Incorrect! Attempts left:", attempts)

if attempts == 0:
    print("Account locked!")
