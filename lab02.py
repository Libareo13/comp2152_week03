# Import the random library to use for the dice rolls
import random

# Define variables
diceOptions = [1, 2, 3, 4, 5, 6]
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Question: Add error handling for combatStrength input, ensuring it is an integer between 1 and 6.
combatStrength = input("Enter your combat Strength (1-6): ")
while not combatStrength.isdigit() or not (1 <= int(combatStrength) <= 6):
    combatStrength = input("Invalid input. Enter your combat Strength (1-6): ")
combatStrength = int(combatStrength)

# Question: Add error handling for the monster's combat strength input, ensuring it is an integer between 1 and 6.
mCombatStrength = input("Enter the monster's combat Strength (1-6): ")
while not mCombatStrength.isdigit() or not (1 <= int(mCombatStrength) <= 6):
    mCombatStrength = input("Invalid input. Enter the monster's combat Strength (1-6): ")
mCombatStrength = int(mCombatStrength)

# Question: Roll the dice (1-6) to determine the hero's health points and display the result.
input("Roll the dice for your health points (Press Enter)")
healthPoints = random.choice(diceOptions)
print(f"You rolled {healthPoints} health points.")

# Question: Roll the dice (1-6) to determine the monster's health points and display the result.
input("Roll the dice for the monster's health points (Press Enter)")
mHealthPoints = random.choice(diceOptions)
print(f"The monster rolled {mHealthPoints} health points.")

# Question: Roll the dice (1-6) to determine if the hero finds a healing potion.
input("Roll the dice to see if you find a healing potion (Press Enter)")
healingPotion = random.choice([0, 1])
print(f"Have you found a healing potion? {'Yes' if healingPotion else 'No'}")

# Question: Roll the dice (1-6) to select a weapon, add its strength to the hero's combat strength, and display feedback.
input("Roll the dice to choose your weapon (Press Enter)")
weaponRoll = random.choice(diceOptions) - 1  # Adjust for 0-based index
combatStrength += weaponRoll
selectedWeapon = weapons[weaponRoll]
print(f"You rolled {weaponRoll + 1} and got the weapon: {selectedWeapon}")

# Question: Define conditions based on the weapon roll and provide appropriate feedback.
if weaponRoll <= 1:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 3:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

if selectedWeapon != "Fist":
    print("Thank goodness you didn't roll the Fist...")

# Question: Simulate a fight between the hero and the monster, displaying the outcomes.
print("You meet the monster. FIGHT!")
input("You strike first (Press Enter)")
if combatStrength >= mHealthPoints:
    print("You've killed the monster!")
else:
    mHealthPoints -= combatStrength
    print(f"You reduced the monster's health to {mHealthPoints}.")
    print("The monster strikes back!")
    if mCombatStrength >= healthPoints:
        print("You're dead!")
    else:
        healthPoints -= mCombatStrength
        print(f"The monster reduced your health to {healthPoints}.")
