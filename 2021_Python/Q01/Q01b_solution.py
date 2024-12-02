#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
Created:   Wed Dec  1 15:01:59 2021
Modified:  Wed Dec  1 15:01:59 2021
"""

# %% Dependencies
import os

# %% Obtain work from previous part
from Q01a_solution import count_increases, values
    
# %% Simple solution on example, does not generalise well.
x = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

if __name__ == '__main__':
    print("\n" + "Simple solution:")
    three_sliding_window = list(zip(x, x[1:], x[2:]))
    window_sum = [sum(i) for i in three_sliding_window]
    count_increases(window_sum)

# %% Chosen solution on example
# Chosen solution
"""
Take advantage of the fact that sum([A, B, C]) - sum([B, C, D]) = A - D,
So for a three sliding window, difference = x[i] - x[i - 3]
"""

def count_increase_window(x, w = 3, verbose = True):
    """
    Generalise NumPy diff method to a bigger lag to find sliding window 
    (of length 'w') differences
    """
    diffs = [x[i] - x[i - w] for i in range(w, len(x))]
    
    n_pos = sum([d >  0 for d in diffs])
    n_neg = sum([d <  0 for d in diffs])
    n_zer = sum([d == 0 for d in diffs])
    
    if verbose:
        print(f"Length    = {len(x):5.0f}")
        print(f"Increases = {n_pos:5.0f}")
        print(f"Decreases = {n_neg:5.0f}")
        print(f"No change = {n_zer:5.0f}")
    
    return n_pos

if __name__ == '__main__':
    print("\n" + "Chosen solution:")
    count_increase_window(x, w = 3, verbose = True)

# %% Calculate answer
if __name__ == '__main__':
    print("\n" + "Chosen solution (non-example):")
    count_increase_window(values, w = 3, verbose = True)
