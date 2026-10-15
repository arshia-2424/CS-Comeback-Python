# CS Comeback - Day 4
# Lists, Sorting, Searching and Statistics

players = ["XANTARES", "donk", "m0NESY", "NiKo"]

# Display all players
for player in players:
    print(player)

# Sort alphabetically (case-insensitive)
sorted_players = sorted(players, key=str.lower)
print("Sorted players:", sorted_players)

# Search for a player
search = input("Enter player name: ")

if search.lower() in [p.lower() for p in players]:
    print("Player found!")
else:
    print("Player not found!")

# Player statistics
kills = [24, 18, 30, 15, 27]

print("Highest kills:", max(kills))
print("Lowest kills:", min(kills))
print("Average kills:", sum(kills) / len(kills))
print("Total players:", len(kills))
