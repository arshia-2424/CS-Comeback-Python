players = ["XANTARES", "donk", "m0NESY", "NiKo"]
new_player = input("Enter the name of the new player: ").strip().lower()
for player in players:
    if new_player == player.lower():
        print(f"{new_player} is already in the list.")
        break
else:
    players.append(new_player)
    print(f"{new_player} has been added to the list.")
    print("Updated list of players:", players)


    