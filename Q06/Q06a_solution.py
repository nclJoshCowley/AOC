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
with open('Q06_eg.txt', 'r') as file:
    population_eg = [int(i) for i in file.read().split(',')]
    
with open('Q06_data.txt', 'r') as file:
    population = [int(i) for i in file.read().split(',')]

# %% 
def iterate_population(x, reset = 6, new = 8):    
    # Decrease by 1 looping back to 'reset' for -1 values
    x_dec = [xi - 1 for xi in x]
    x_out = [reset if xd == -1 else xd for xd in x_dec]
    
    # Add 'NEW' fish
    for n in range(sum([xi == 0 for xi in x])):
        x_out.append(new)
        
    return x_out
        
# %% 
def sim_n_days(population, n):
    pop = population
    
    for ni in range(n):
        # print(f"After {ni:2.0f} days (len = {len(pop)}):\n{pop}\n")
        print(f"After {ni:2.0f} days (len = {len(pop)})\n")
        pop = iterate_population(pop)
    
    ni += 1
    print(f"After {ni:2.0f} days (len = {len(pop)})\n")
    return len(pop)
        
# %% Run code on both inputs    
if __name__ == '__main__':
    sim_n_days(population_eg, n = 18)
    sim_n_days(population_eg, n = 80)
    
    ans = sim_n_days(population, n = 80)
        