"""
Brock Nebeker
IS 303- A02

Quest Recommeneder
This program suggests a quest based on the player's class and level

Inputs:
- Level
- Class

Processes:
- If the level is negative print an error message
- If the class isn't an option listed then print an error message
- Find the level range
- First go by level range then by class

Outputs:
- Recommended quest
- Error message if there is an invalid input
"""
# Inputs
player_class = input("Class: Warrior/Mage/Rogue ").lower()
level = int(input("Level: "))

# Processes
classes = ["warrior", "mage", "rogue"]

# Outputs
if player_class not in classes:
    print("Error: Class must be either Warrior, Mage, or Rogue.")
elif level <= 0:
    print("Error: Level must be 1 or greater.")
else:
    if level < 11:
        if player_class == "warrior":
            print(f"CLASS: {player_class.upper()}")
            print(f"LEVEL: {level}")
            print("Take down an ogre.")
        elif player_class == "mage":
            print(f"CLASS: {player_class.upper()}")
            print(f"LEVEL: {level}")
            print("Use a fireball spell.")
        else:
            print(f"CLASS: {player_class.upper()}")
            print(f"LEVEL: {level}")
            print("Track down a caravan.")
    elif level < 26:
        if player_class == "warrior":
            print(f"CLASS: {player_class.upper()}")
            print(f"LEVEL: {level}")
            print("Collect a high level sword.")
        elif player_class == "mage":
            print(f"CLASS: {player_class.upper()}")
            print(f"LEVEL: {level}")
            print("Use a lightning spell.")
        else:
            print(f"CLASS: {player_class.upper()}")
            print(f"LEVEL: {level}")
            print("Spy on a local warlord.")
    else:
        if player_class == "warrior":
            print(f"CLASS: {player_class.upper()}")
            print(f"LEVEL: {level}")
            print("Take down a dragon.")
        elif player_class == "mage":
            print(f"CLASS: {player_class.upper()}")
            print(f"LEVEL: {level}")
            print("Use a teleportation spell.")
        else:
            print(f"CLASS: {player_class.upper()}")
            print(f"LEVEL: {level}")
            print("Find long lost treasure.")
