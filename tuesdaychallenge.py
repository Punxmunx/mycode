#!/usr/bin/python3
def main():
    #list for reference
    mylist = [1,2,3,4,5,"Python"]
    # likely the function
    name = input("What is your name?")

    # This is what you should see when print runs-
    # Hi <name>! Welcome to Day 2 of Python Training!
    print("Hi", name.capitalize() + "!", "Welcome to Day", mylist[1], "of", mylist[5], "Training!")
main()
