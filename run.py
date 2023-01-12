"""
Libraries 
"""

import random
from graphicstuff import welcome

def intro_screen():
    """
    intro strings
    """
    print(welcome)

intro_screen()

def parse_input(input_string):
    if input_string.strip() in {"1", "2", "3"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 and 3")
        raise SystemExit(1)

di_input = input("How many dice do you want to roll? [1-3]\n")
di_num = parse_input(di_input)







   
