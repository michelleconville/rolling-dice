"""
Libraries 
"""

import random
from graphicstuff import welcome

di_input = input("How many dice do you want to roll? [1-3]\n")
di_num = parse_input(di_input)

def parse_input(input_string):
    if input_string.strip() in {"1", "2", "3"}:
        return int(input_string)
    else:

def intro_screen():
    """
    intro strings
    """
    print(welcome)



   
