print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("=" * 70)
print("🏴‍☠️ WELCOME TO THE ULTIMATE TREASURE HUNT 🏴‍☠️")
print("=" * 70)
print("Mission: Find the Lost King's Treasure before sunset!")
print()

health = 100
inventory = []

# ---------------- Stage 1 ----------------

choice1 = input(
    "You reach a mysterious crossroad.\n"
    "Go LEFT into the dark forest or RIGHT into the cave?\n"
    "(left/right): "
).lower()

if choice1 != "left":
    print("\nYou entered the cave and fell into a hidden pit.")
    print("💀 GAME OVER")
    quit()

print("\n🌳 You enter the forest safely.")

# ---------------- Stage 2 ----------------

choice2 = input(
    "\nA river blocks your path.\n"
    "Do you WAIT for a boat or BUILD a raft?\n"
    "(wait/build): "
).lower()

if choice2 == "wait":
    print("\nA boat arrives safely.")
elif choice2 == "build":
    print("\nYour raft breaks halfway.")
    health -= 30
    print(f"You survived but lost 30 health. Health = {health}")
else:
    print("\nYou got swept away by the river.")
    print("💀 GAME OVER")
    quit()

# ---------------- Stage 3 ----------------

print("\nYou discover three treasure chests.")

chest = input(
    "Choose one:\n"
    "1. Wooden Chest\n"
    "2. Golden Chest\n"
    "3. Black Chest\n"
    "Enter (1/2/3): "
)

if chest == "1":
    print("You found a TORCH!")
    inventory.append("Torch")

elif chest == "2":
    print("You found a GOLDEN KEY!")
    inventory.append("Golden Key")

elif chest == "3":
    print("A poisonous snake bites you!")
    health -= 40
    print(f"Health = {health}")

else:
    print("You walked away without opening any chest.")

# ---------------- Stage 4 ----------------

print("\nA wise old guardian blocks your path.")
print("Answer his riddle.")

riddle = input(
    "\nI have keys but no locks.\n"
    "I have space but no rooms.\n"
    "You can enter but can't go outside.\n"
    "Who am I?\n\n"
).lower()

if riddle == "keyboard":
    print("\nCorrect! The guardian gives you a SWORD.")
    inventory.append("Sword")
else:
    print("\nWrong answer!")
    health -= 20
    print(f"Health = {health}")

if health <= 0:
    print("\nYou collapsed from your injuries.")
    print("💀 GAME OVER")
    quit()

# ---------------- Stage 5 ----------------

print("\nYou finally reach the Treasure Temple.")

door = input(
    "There are three magical doors.\n"
    "Red\n"
    "Blue\n"
    "Golden\n"
    "Choose one: "
).lower()

if door == "red":
    print("\n🔥 The room bursts into flames.")
    print("GAME OVER")

elif door == "blue":
    if "Sword" in inventory:
        print("\nA giant monster attacks!")
        print("⚔️ You defeat it with your Sword.")
        print("Behind it lies the King's Treasure!")
        print("\n🏆 CONGRATULATIONS! YOU WIN!")
    else:
        print("\nA giant monster eats you.")
        print("💀 GAME OVER")

elif door == "golden":
    if "Golden Key" in inventory:
        print("\n🔑 You unlock the Golden Door.")
        print("Inside are mountains of gold and diamonds!")
        print("🏆 YOU FOUND THE LEGENDARY TREASURE!")
        print("\n★★★★★ TRUE ENDING ★★★★★")
    else:
        print("\nThe Golden Door is locked forever.")
        print("GAME OVER")

else:
    print("\nThat door doesn't exist.")
    print("GAME OVER")

# ---------------- Summary ----------------

print("\n" + "=" * 60)
print("Adventure Summary")
print("=" * 60)
print(f"Health Left : {health}")
print(f"Inventory   : {inventory}")
print("=" * 60)