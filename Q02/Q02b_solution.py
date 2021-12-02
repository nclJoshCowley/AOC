#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
What does this script do?

@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
Created:   Thu Dec  2 14:45:25 2021
Modified:  Thu Dec  2 14:45:25 2021
"""

# %% Dependencies
import re
from Q02a_solution import lines

# %% Re-use code from first part
def input_to_action_value(x):
    regex = re.compile(r"(\w+) (\d+)")    
    matches = [regex.match(xi) for xi in x]
    
    actions = [m.group(1) for m in matches]
    values  = [int(m.group(2)) for m in matches]
    
    return actions, values

# %% Simplify by losing historical data :(
def input_to_aimed_horiz_depth(x):    
    actions, values = input_to_action_value(x)
    
    aim, horiz, depth = 0, 0, 0
    
    for i in range(len(actions)):
        if actions[i] == "down":
            aim += values[i]
        elif actions[i] == "up":
            aim -= values[i]
        elif actions[i] == "forward":
            horiz += values[i]
            depth += aim * values[i]
        else: 
            raise ValueError
            
    return horiz, depth

# %% Test on worked example
if __name__ == '__main__':
    eg = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    h, d = input_to_aimed_horiz_depth(eg)
    print(f"Final horizontal position = {h:5.0f}")
    print(f"Final depth      position = {d:5.0f}")
    print(f"Product of both positions = {h*d:5.0f}")

# %% Apply to given input
if __name__ == '__main__':
    print("\n")
    h, d = input_to_aimed_horiz_depth(lines)
    print(f"Final horizontal position = {h:10.0f}")
    print(f"Final depth      position = {d:10.0f}")
    print(f"Product of both positions = {h*d:10.0f}")
