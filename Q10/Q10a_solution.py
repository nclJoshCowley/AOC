#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
"""

# %% Dependencies
import numpy as np


# %% Read from file
def read_from_file(path):
    with open(path, "r") as file:
        lines = file.read().split("\n")

    return lines


# %% Globals relating to bracket parsing
b_vals = {"(": 0, "[": 1, "{": 2, "<": 3, ")": 5, "]": 6, "}": 7, ">": 8}
v_brac = {v:k for (k, v) in b_vals.items()}

# %%
if __name__ == "__main__":
    lines = read_from_file("Q10_eg.txt")
    cur_line = lines[0]
    
    for cur_ch in iter(cur_line):
        unmatched_brackets = []
        
        if bracs[cur_ch] < 5:
            unmatched_brackets.append(cur_ch)
        else:
            # Need to check valid closing bracket and pop from running list
            # Time issue, worked for <20 mins. :(
    
    
