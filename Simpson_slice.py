#!/usr/bin/env python3
"""simpsons slicing challenge"""
# will be an attempt to slice an splice up a dictionary list as practice while building skills for the project 
def main():

#lists to refer to 
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
   #using challenge list print My eyes! The goggles do nothing!
    a=challenge[2][1]
    b=challenge[2][0]
    c=challenge[3]
    print(f"My {a}! the {b} do {c}!")
   #using trial list print My eyes! The goggles do nothing!
    a=trial[2]["goggles"]
    b=trial[2]["eyes"]
    c=trial[-1]
    print(f"My {a} the {b} do {c}!")
   #using nightare list print My eyes! The goggles do nothing!
    a=nightmare[0]["user"]["name"]["first"]
    b=nightmare[0]["kumquat"]
    c=nightmare[0]["d"]
    print(f"My {a} the {b} do {c}!") 

main()
