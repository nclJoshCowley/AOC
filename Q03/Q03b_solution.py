#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk 
"""

# %% Dependencies
import numpy as np
from Q03a_solution import lines, binary_list_to_int


# %% Easier with NumPy arrays?
def input_to_array(x):
    strlen = len(x[0])

    bit_array = np.zeros((len(x), strlen))

    for i, x_str in enumerate(x):
        x_lst = [int(x_str[j]) for j in range(len(x_str))]
        bit_array[i,] = np.array(x_lst)
        
    return bit_array

# %% FUNCITON: Get most common bit from a series of values
def get_most_common_bit(z, flip):
    n1s = sum(z)
    n0s = len(z) - n1s
    mcb = int(n1s >= n0s)
    
    if flip:
        return 1 - mcb
    else:
        return mcb
    
# %%
def get_rating(x, flip):
    c_bit = 0

    while x.shape[0] > 1:
        mcb = get_most_common_bit(x[:,c_bit], flip)
        is_kept = x[:, c_bit] == mcb
        x = x[is_kept, :]
        c_bit += 1
        
    return x[0, :]

# %% Combine into script-like function
def part_b(x):
    o2_np = get_rating(input_to_array(x), flip = False)
    co2_np = get_rating(input_to_array(x), flip = True)

    o2 = binary_list_to_int(o2_np)
    co2 = binary_list_to_int(co2_np)

    print(f"O2 rate   = {o2:8.0f}")
    print(f"C02 rate  = {co2:8.0f}")
    print(f"Product   = {o2 * co2:8.0f}")
        
# %% Worked example
if __name__ == '__main__':
    eg = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    part_b(eg)

# %% On given input
if __name__ == '__main__':
    print("\n")
    part_b(lines)

