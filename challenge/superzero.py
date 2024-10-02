#!/usr/bin/env python3
"""Superhero statistics viewer."""

def main():
    # Define a dictionary with superhero characters and their details
    marvelchars = {
        "Starlord": {
            "real name": "peter quill",
            "powers": "dance moves",
            "archenemy": "Thanos"
        },
        "Mystique": {
            "real name": "raven darkholme",
            "powers": "shape shifter",
            "archenemy": "Professor X"
        },
        "Hulk": {
            "real name": "bruce banner",
            "powers": "super strength",
            "archenemy": "adrenaline"
        }
    }

    # Get the character name from user input
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): ")
    
    # Check if the character exists in the dictionary
    if char_name in marvelchars:
        # Get the statistic type from user input
        char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ").lower()
        
        # Check if the requested statistic exists for the character
        if char_stat in marvelchars[char_name]:
            value = marvelchars[char_name][char_stat]
            # Print the requested statistic
            print(f"{char_name}'s {char_stat} is: {value}")
        else:
            # Handle the case where the statistic is not valid
            print(f"Sorry, {char_stat} is not a valid statistic for {char_name}.")
    else:
        # Handle the case where the character is not valid
        print(f"Sorry, {char_name} is not a valid character.")

# Run the main function
main()

