#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
"""

# %% Dependencies
import numpy as np
# import functools
    
# %% Read from file
with open('Q05_eg.txt', 'r') as file:
    lines_eg = file.read().splitlines()
    
with open('Q05_data.txt', 'r') as file:
    lines = file.read().splitlines()

# %% Convert text to integer coordinates of endpoints
def lines_to_endpoints(x):
    x_split = [xi.split(' -> ') for xi in x]
    
    start_pts_chr = [xs[0].split(',') for xs in x_split]
    start_pts = [[int(ch) for ch in l] for l in start_pts_chr]
    
    end_pts_chr = [xs[1].split(',') for xs in x_split]
    end_pts = [[int(ch) for ch in l] for l in end_pts_chr]
    
    return start_pts, end_pts
    
# %% Get list of coords from endpoints
def endpoints_to_coords_covered(start, end):
    x1, y1 = start
    x2, y2 = end
    
    if x1 == x2:
        y_range = range(min(y1, y2), max(y1, y2) + 1)
        return [(x1, y) for y in y_range]
    elif y1 == y2:
        x_range = range(min(x1, x2), max(x1, x2) + 1)
        return [(x, y1) for x in x_range]
    else:
        return None
    
# %% 
def count_coords(coords, quiet = False):
    x_max = max([c[0] for c in coords])
    y_max = max([c[1] for c in coords])
    counter = np.zeros((y_max + 1, x_max + 1))
    
    for xi, yi in coords:
        counter[yi, xi] += 1
        
    if not quiet:
        print("\n", counter)
    return counter
    

# %% Unit test of function so far
if __name__ == '__main__':
    tst_input = ["0,7 -> 5,7", "2,1 -> 2,9"]
    tst_strt, tst_end = lines_to_endpoints(tst_input)
    
    tst_coords = [endpoints_to_coords_covered(s, e) for s, e in zip(tst_strt, tst_end)]
    tst_coords = [i for l in tst_coords for i in l]
    
    count_coords(tst_coords)
    
def part_a(llines):
    strt, end = lines_to_endpoints(llines)
    
    coords_list = [endpoints_to_coords_covered(s, e) for s, e in zip(strt, end)]
    coords_list = [i for i in coords_list if i]
    coords = [i for l in coords_list for i in l if i]
    
    count = count_coords(coords)
    print(f"\nSum of 2's = {(count >= 2).sum()}")
    

    
# %% Run code on both inputs    
if __name__ == '__main__':
    part_a(lines_eg)
    part_a(lines)
        