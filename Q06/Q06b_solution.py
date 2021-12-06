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

# %% Previous solution runs out memory on example
# New solution: Keep running counts
def part_b(x, days, quiet = False):
    running_count = np.zeros(9, dtype = 'int64')
        
    for xi in x:
        running_count[xi] += 1
    
    for d in range(days):
        if not quiet:
            print(f"Day {d:3.0f}. No. of fish = {sum(running_count)}")
        
        new_fish = running_count[0]
        
        # Fish at 0 resets to 8 (not 6) so we correct by adding to count of 6
        running_count = np.roll(running_count, -1)
        running_count[6] += new_fish
    
    print(f"\n\nDay {d + 1:3.0f}. No. of fish = {sum(running_count)}")
    return sum(running_count)



# %% Run code on both inputs    
if __name__ == '__main__':    
    part_b(population_eg, days = 18)
    part_b(population_eg, days = 80, quiet = True)
    part_b(population_eg, days = 256, quiet = True)
    
    part_b(population, days = 256, quiet = True)
    
        