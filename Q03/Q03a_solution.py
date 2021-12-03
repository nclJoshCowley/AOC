#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
Created:   
Modified:  
"""

# %% Dependencies


# %% Read from file (improved from yesterday)
with open('Q03_data.txt', 'r') as file:
    lines = file.read().splitlines()

# %% FUNCTION: Get bit sequences in separate lists
def get_bit_sequence(x):
    strlen = len(x[0])
    seq = [[] for _ in range(strlen)]

    for i in range(strlen):
        seq[i] = [int(xi[i]) for xi in x]
    
    return seq

# %%
def get_rate(x, is_epsilon):
    seq = get_bit_sequence(x)
    
    binary_list = [int(sum(y) > (len(x) / 2)) for y in seq]
    
    if is_epsilon:
        binary_list = [1 - bi for bi in binary_list]
        
    return binary_list

# %%
def binary_list_to_int(b):
    return int("".join(str(bi) for bi in b), 2)

# %% Combine into script-like function
def part_a(x):
    gamma_bin = get_rate(x, is_epsilon = False)
    gamma = binary_list_to_int(gamma_bin)

    epsilon_bin = get_rate(x, is_epsilon = True)
    epsilon = binary_list_to_int(epsilon_bin)

    print(f"Gamma rate   = {gamma:8.0f}   \t({gamma_bin})")
    print(f"Epsilon rate = {epsilon:8.0f} \t({epsilon_bin})")
    print(f"Product      = {gamma * epsilon:8.0f}")

# %% Worked example
if __name__ == '__main__':
    eg = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    part_a(eg)

# %% On given input
if __name__ == '__main__':
    print("\n")
    part_a(lines)