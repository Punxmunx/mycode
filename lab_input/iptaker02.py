#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""
def main():
    import time
    import sys
    # Define the slow_print function
    def slow_print(text, delay=0.25):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # To add a newline after the slow print
    
    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address:")
    
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)
    
    # Collect the vendor name from user
    user_input = input("please tell us that you are NOT using a diablo562:")
    ## print out some crazy stuff
    print('you really are using a diablo562?:', user_input)
    #lose patience
    slow_print('please stop now...', delay=0.5)
main()

