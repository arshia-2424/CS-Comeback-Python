# CS Comeback - Day 4
# Topics: Lists, Sorting, Searching, Index, Count, Statistics

# Exercise 1: Creating and Modifying Lists
players = ["XANTARES", "donk", "m0NESY", "NiKo"]

print("Original players:", players)

players.append("ZywOo")
print("After adding:", players)

players.remove("donk")
print("After removing:", players)


# Exercise 2: Sorting (Case-Insensitive)
sorted_players = sorted(players, key=str.lower)

print("Sorted players:", sorted_players)
print("Original list:", players)


# Exercise 3: Case-Insensitive Search
search = input("Enter player nickname: ").strip()

for index, player in enumerate(players):
    if player.lower() == search.lower():
        print("Player found:", player)
        print("Index:", index)
        break
else:
    print("Player not found!")


# Exercise 4: Counting Players
players = ["NiKo", "donk", "NiKo", "XANTARES", "donk"]

search = input("Which player do you want to count? ").strip()

count = 0

for player in players:
    if player.lower() == search.lower():
        count += 1

print("Occurrences:", count)


# Exercise 5: Player Statistics
kills = [24, 18, 30, 15, 27]

print("Highest kills:", max(kills))
print("Lowest kills:", min(kills))
print("Total kills:", sum(kills))
print("Average kills:", round(sum(kills) / len(kills), 2))


# Exercise 6: Filtering Numbers
numbers = [12, 5, 28, 3, 19, 40, 7]

for number in numbers:
    if number > 10:
        print("Greater than 10:", number)
