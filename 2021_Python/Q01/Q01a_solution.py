#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
Created:   Wed Dec  1 14:17:05 2021
Modified:  Wed Dec  1 15:01:09 2021
"""

# %% Dependencies
import numpy as np

# %% Read values from file
with open('Q01_data.txt', 'r') as file:
    lines = file.readlines()
    values = [int(l.rstrip("\n")) for l in lines]
    
# %% Function definition    
def count_increases(x, verbose = True):
    """
    Through NumPy's diff() method we count how many times a series increases
    """
    diffs = np.diff(x)
    
    n_pos = sum([d >  0 for d in diffs])
    n_neg = sum([d <  0 for d in diffs])
    n_zer = sum([d == 0 for d in diffs])
    
    if verbose:
        print(f"Length    = {len(x):5.0f}")
        print(f"Increases = {n_pos:5.0f}")
        print(f"Decreases = {n_neg:5.0f}")
        print(f"No change = {n_zer:5.0f}")
    
    return n_pos

# %% Example test
# Test on example, answer should be 7
if __name__ == '__main__':
    print("\n" + "Chosen solution (example):")
    count_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], verbose = True)
    
# %% Calculate answer
if __name__ == '__main__':
    print("\n" + "Chosen solution (non-example):")
    count_increases(values, verbose = True)
