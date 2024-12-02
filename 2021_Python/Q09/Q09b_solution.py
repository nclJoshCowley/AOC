#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
"""

# %% Dependencies
import numpy as np
from functools import reduce
from Q09a_solution import read_from_file, get_neighbours, is_low_point

# %%
def find_low_points(arr):
    low_pts = []
    
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if is_low_point(arr, i, j):
                low_pts.append((i, j))

    return low_pts

# %%
def peek_value(pt, arr, direction):
    # Surround array with 9s (boundaries)
    arr_pad = np.pad(arr, 1, constant_values = 9)
    
    # All the 1 + () is padding correction
    if direction == "N":
        return arr_pad[1 + (pt[0] - 1), 1 + (pt[1])]
    elif direction == "S":
        return arr_pad[1 + (pt[0] + 1), 1 + (pt[1])]
    elif direction == "E":
        return arr_pad[1 + (pt[0]), 1 + (pt[1] + 1)]
    elif direction == "W":
        return arr_pad[1 + (pt[0]), 1 + (pt[1] - 1)]
    else:
        raise ValueError
        
# %%
def find_basin(lp, arr):
    store = []
    seek = [lp]
    
    while len(seek) > 0:
        cur_seek = seek[0]
        store.append(cur_seek)
        seek.remove(cur_seek)
        
        # Following could do with a refactor
        # It adds all non 9 or boundary coords to 'seek'
        if peek_value(cur_seek, arr, "N") != 9:
            seek.append((cur_seek[0] - 1, cur_seek[1]))
        if peek_value(cur_seek, arr, "S") != 9:
            seek.append((cur_seek[0] + 1, cur_seek[1]))
        if peek_value(cur_seek, arr, "E") != 9:
            seek.append((cur_seek[0], cur_seek[1] + 1))
        if peek_value(cur_seek, arr, "W") != 9:
            seek.append((cur_seek[0], cur_seek[1] - 1))
            
        # Remove already seeked values
        for st in store:
            if st in seek:
                seek.remove(st)
                
    return store

# %%
if __name__ == "__main__":
    arr = read_from_file("Q09_eg.txt")
    low_pts = find_low_points(arr)

    find_basin((0, 1), arr)
    find_basin((0, 9), arr)
    find_basin((2, 2), arr)
    find_basin((4, 6), arr)
    
    del arr, low_pts
    
# %% Part (b)
def part_b(path):
    arr = read_from_file(path)
    low_pts = find_low_points(arr)
    
    basin_sizes = [len(find_basin(lp, arr)) for lp in low_pts]
    top_3_basin_sizes = sorted(basin_sizes, reverse = True)[:3]
    return np.prod(top_3_basin_sizes)

if __name__ == "__main__":
    print(f"Example product = {part_b('Q09_eg.txt')}")
    print(f"Input   product = {part_b('Q09_data.txt')}")
    


