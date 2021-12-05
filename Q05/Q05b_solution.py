#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
"""

# %% Dependencies
import numpy as np
import functools
from Q05a_solution import lines, lines_eg, lines_to_endpoints, count_coords


# %% Fix 1: Order important on digaonals, replace range(min(), max() + 1)
def ordered_range(z1, z2):
    if z1 <= z2:
        return range(z1, z2 + 1)
    else:
        return range(z1, z2 - 1, -1)
    
# %% Changes need to be made to:
def endpoints_to_coords_covered_new(start, end):
    x1, y1 = start
    x2, y2 = end
    
    # Change 1: Pull range definition out of if-elif-else flow    
    y_range = ordered_range(y1, y2)
    x_range = ordered_range(x1, x2)
    # <--
   
    if x1 == x2:
        return [(x1, y) for y in y_range]
    elif y1 == y2:
        return [(x, y1) for x in x_range]
    elif abs(x2 - x1) == abs(y2 - y1):
        # Change 2: None hozirontal and vertical case is 45 deg only
        return list(zip(x_range, y_range))
        # <--

# Unit test(s)
if __name__ == '__main__':
    print(endpoints_to_coords_covered_new([1, 1], [1, 3])) # x fixed
    print(endpoints_to_coords_covered_new([3, 3], [1, 3])) # y fixed
    print(endpoints_to_coords_covered_new([1, 1], [3, 3])) # diagonal
    # Issue
    print(endpoints_to_coords_covered_new([8, 0], [0, 8]))
    
        
# %% Copy from part (a) with minor improvements
def part_b(llines):
    strt, end = lines_to_endpoints(llines)
    
    coords_list = [endpoints_to_coords_covered_new(s, e) for s, e in zip(strt, end)]
    coords = [i for l in coords_list for i in l if i]
    
    count = count_coords(coords)
    print(f"\nSum of 2's = {(count >= 2).sum()}")

# %% Run code on both inputs    
if __name__ == '__main__':
    part_b(lines_eg)
    part_b(lines)