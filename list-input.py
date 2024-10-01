#!/usr/bin/env python3
"""alta fun | lists challenge"""

#import random module
import random

def main():
#main function and reference data
    wordbank= ["indentation", "spaces"]
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
    print(tlgstudents)
    # append and  print new wordbank
    wordbank.append(4)
    print(wordbank)
    # changing class sizes
    num = int(input(f"Enter a student number between 1 and {len(tlgstudents)} --> "))-1
    name = tlgstudents[num]
    print(f"your unfortunate victim is {name}!")
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")
    name= random.choice(tlgstudents)
    print(f"{name}")
if __name__== "__main__":
    main()
