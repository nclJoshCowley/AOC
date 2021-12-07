#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
"""

# %% Dependencies
import numpy as np
from Q07a_solution import dist, brute_force, positions, positions_eg

# %% Define the new metric
def tri_dist(x, n):
    raw_dists = [abs(xi - n) for xi in x]
    tri_dists = [sum(range(1, rd + 1)) for rd in raw_dists]
    return sum(tri_dists)

# %%
if __name__ == '__main__':
    arg, lst = brute_force(positions_eg, tri_dist)
    print(f"Position = {arg:4.0f}, Fuel = {lst[arg]:4.0f}")

    arg, lst = brute_force(positions, tri_dist)
    print(f"Position = {arg:4.0f}, Fuel = {lst[arg]:4.0f}")
    
        