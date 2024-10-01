#! /usr/bin/python3
 #use if else elif

# Define the monster's hit types
monster_hits = ["roll", "spark", "enlighten"]

# Introduction
print("Let's see if your skills enlighten the monster!")
print("Enter three ritals from the following options: roll, spark, enlighten")

# Get user inputs for three hits
hit1 = input("Enter your first hit: ").lower()
hit2 = input("Enter your second hit: ").lower()
hit3 = input("Enter your third hit: ").lower()

# Check if the user inputs match the monster's hits
if hit1 == monster_hits[0] and hit2 == monster_hits[1] and hit3 == monster_hits[2]:
    print("You rolled the monster! Great job!")
elif hit1 == monster_hits[0] and hit2 == monster_hits[1]:
    print("Almost there! You got the roll  and spark right, but missed the enlighten.")
elif hit1 == monster_hits[1]:
    print("You got the spark right, but need to work on the others.")
elif hit1 != "cough" and hit2 != "gag" and hit3 != "die":
    print("None of your skills enlightened the monster! Try again.")
else:
    print("Close, but not quite. You need to match all three rituals to enlighten the monster!")

print("Thanks for playing!")
