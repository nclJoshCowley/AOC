#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
"""

# %% Dependencies
import numpy as np
    
# %% Read from file
positions_eg = [16,1,2,0,4,2,7,1,2,14]
    
with open('Q07_data.txt', 'r') as file:
    positions = [int(i) for i in file.read().split(',')]

# %% Define (summed) distance between vector x and candidate n
def dist(x, n):
    return sum([abs(xi - n) for xi in x])

# %% Brute force by looping through all possible 'n'
def brute_force(x, dist_fn):
    out = [dist_fn(x, ni) for ni in range(max(x))]
    return np.argmin(out), out

# %%
if __name__ == '__main__':
    arg, lst = brute_force(positions_eg, dist)
    print(f"Position = {arg:4.0f}, Fuel = {lst[arg]:4.0f}")

    arg, lst = brute_force(positions, dist)
    print(f"Position = {arg:4.0f}, Fuel = {lst[arg]:4.0f}")
    