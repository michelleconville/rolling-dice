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
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 and 3")
        raise SystemExit(1)

def roll_dice(di_num):
    roll_results = []

    for _ in range(di_num):
        roll = random.randint(1,6)
        roll_results.append(roll)
    return roll_results


di_input = input("How many dice do you want to roll? [1-3]\n")
di_num = parse_input(di_input)
roll_results = roll_dice(di_num)
print(roll_results)







   
