#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
Created:   Thu Dec  2 14:12:07 2021
Modified:  Thu Dec  2 14:44:49 2021
"""

# %% Dependencies
import re

# %% Read from file (improved from yesterday)
with open('Q02_data.txt', 'r') as file:
    lines = file.read().splitlines()
    
# %% Define function  
def input_to_horiz_depth(x):
    regex = re.compile(r"(\w+) (\d+)")    
    matches = [regex.match(xi) for xi in x]
    
    actions = [m.group(1) for m in matches]
    values  = [int(m.group(2)) for m in matches]
    
    horiz = [0 for i in range(len(x))]
    depth = [0 for i in range(len(x))]
    for i in range(len(x)):
        if actions[i] == "forward":
            horiz[i] = values[i]
        elif actions[i] == "down":
            depth[i] = values[i]
        elif actions[i] == "up":
            depth[i] = -values[i]
            
    return horiz, depth

# %% Test on worked example
if __name__ == '__main__':
    eg = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    h, d = input_to_horiz_depth(eg)
    ans = sum(h) * sum(d)
    print(f"Final horizontal position = {sum(h):5.0f}")
    print(f"Final depth      position = {sum(d):5.0f}")
    print(f"Product of both positions = {ans:5.0f}")

# %% Apply to given input
if __name__ == '__main__':
    print("\n")
    h, d = input_to_horiz_depth(lines)
    ans = sum(h) * sum(d)
    print(f"Final horizontal position = {sum(h):7.0f}")
    print(f"Final depth      position = {sum(d):7.0f}")
    print(f"Product of both positions = {ans:7.0f}")

