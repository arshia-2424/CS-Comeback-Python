name = input("Please enter your name: ")
age = int(input("Please enter your age: "))


if age < 0:
    print(f"Hello {name}, Invalid age. Age cannot be negative.")
elif age < 18:
    print(f"Hello {name}, you are too young.")
elif age <= 64:
    print(f"Hello {name}, you are an adult.")
else:
    print(f"Hello {name}, you are a senior.")

#for → repeat a known amount/range.
#while → repeat until a condition changes.


username = input("Enter your username: ")
password = input("Enter your password: ")

while username != "admin" or password != "python123":
    print("Incorrect username or password. Try again.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
print("Access granted. Welcome admin!")

name = input("Enter your name: ")
age = int(input("Please enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").strip().lower()

if age >= 18 and has_id == "yes":
    print(f"Welcome {name}!")
elif age < 18:
    print(f"sorry {name}, you are too young.")
elif age >=18 and has_id != "yes":
    print(f"sorry {name}, you need id.")
else:
    print(f"sorry {name}, entry denied.")


games = ["Cs2", "GTA", "Minecraft", "valorant"]

for game in games:
    print(game)

players = [name.lower() for name in ["XANTARES", "donk", "m0NESY", "NiKo"]]
player_name = input("Enter the player name: ").strip().lower()
if player_name in players:
    print("Player found!")
else:
    print("Player not found.")