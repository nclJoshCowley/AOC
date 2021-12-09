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
    
    rows = [l.strip("\n") for l in lines]
    
    arr = np.array([[int(el) for el in rw] for rw in rows])
    
    return arr

# %%
def get_neighbours(arr, i, j):
    out = []
    
    # Vertical neighbours (on rows)
    if i > 0:
        out.append(arr[i - 1, j])
    if i < (arr.shape[0] - 1):
        out.append(arr[i + 1, j])
    
    # Horizontal neighbours (on cols)
    if j > 0:
        out.append(arr[i, j - 1])
    if j < (arr.shape[1] - 1):
        out.append(arr[i, j + 1])
        
    return out
        
def is_low_point(arr, i, j):
    near = get_neighbours(arr, i, j)
    return all(arr[i, j] < near)

# %% Part (a)
def part_a(path):
    array = read_from_file(path)
    low_pts = []
    
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if is_low_point(array, i, j):
                low_pts.append(array[i, j])

    risk_pts = [lp + 1 for lp in low_pts]
    return sum(risk_pts)

# %%
if __name__ == "__main__":
    print(f"Example Risk score = {part_a('Q09_eg.txt')}")
    print(f"Input   Risk score = {part_a('Q09_data.txt')}")
