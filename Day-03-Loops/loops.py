# CS Comeback - Day 3
# Topics: For, While, Range, Break, Continue, Lists

# Exercise 1: Numbers from 1 to 10
for i in range(1, 11):
    print(i)


# Exercise 2: Numbers Greater Than 5
for i in range(1, 11):
    if i > 5:
        print(i)


# Exercise 3: Countdown
count = 10

while count > 0:
    print(count)
    count -= 1

print("Countdown finished!")


# Exercise 4: Password Attempts
correct_password = "1234"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful!")
        break

    attempts -= 1
    print("Incorrect! Attempts left:", attempts)
else:
    print("Account locked!")


# Exercise 5: Searching Players
players = ["XANTARES", "donk", "m0NESY", "NiKo"]

search = input("Search for a player: ").strip()

for player in players:
    if player.lower() == search.lower():
        print("Player found:", player)
        break
else:
    print("Player not found!")


# Exercise 6: Skip Numbers
for number in range(1, 11):
    if number == 5:
        continue

    print(number)
