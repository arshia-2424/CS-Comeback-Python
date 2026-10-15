# CS Comeback - Day 1
# Topics: Variables, Data Types, Input, Calculations

# Exercise 1: Player Statistics
player = "XANTARES"
kills = 24
deaths = 15

print(player)
print(kills)
print(deaths)

difference = kills - deaths
print("Kill difference:", difference)


# Exercise 2: Favourite Game
game = input("What is your favourite game? ")
print("Favourite game:", game)


# Exercise 3: K/D Calculator
user_kills = int(input("How many kills did you get? "))
user_deaths = int(input("How many deaths did you get? "))

user_difference = user_kills - user_deaths

if user_deaths > 0:
    user_kd = user_kills / user_deaths
    print("K/D Ratio:", round(user_kd, 2))
else:
    print("K/D Ratio: Undefined (zero deaths)")

print("Kill difference:", user_difference)


# Exercise 4: Complete Player Statistics
player_name = input("What is your nickname? ")
player_kills = int(input("How many kills did you get? "))
player_deaths = int(input("How many deaths did you get? "))
player_assists = int(input("How many assists did you get? "))

print("Player:", player_name)
print("Kills:", player_kills)
print("Deaths:", player_deaths)
print("Assists:", player_assists)

if player_deaths > 0:
    player_kd = player_kills / player_deaths
    print("K/D Ratio:", round(player_kd, 2))
else:
    print("K/D Ratio: Undefined")
