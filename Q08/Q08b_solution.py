#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
"""

# %% Dependencies
from functools import reduce
from Q08a_solution import read_from_file, lookup_digit_length

# %% Utility
def string_diff(s1, s2):
    s1_set = set([s for s in s1])
    s2_set = set([s for s in s2])
    return "".join(s1_set - s2_set)

def string_intresect(s1, s2):
    s1_set = set([s for s in s1])
    s2_set = set([s for s in s2])
    return "".join(s1_set.intersection(s2_set))
    

# %% Temp script
path = "Q08_eg.txt"
patterns, output = read_from_file(path)

ptn = patterns[0]
out = output[0]

filter_len = lambda x, l: [xi for xi in x if len(xi) == l]
len_to_ptn = {l:filter_len(ptn, l) for l in range(2,8)}


# Goes from mixed letter 'd' to original letter in prompt 'a'
lookup_original = {}

# Find original 'a' difference between 1 and 7
new_a = string_diff(len_to_ptn[3][0], len_to_ptn[2][0])
lookup_original[new_a] = "a"

# Find original 'g' by noticing its presence in all but 1, 4, 7
not_147 = [p for i in (5, 6) for p in len_to_ptn[i]]
new_g = reduce(string_intresect, not_147).strip(new_a)
lookup_original[new_g] = "g"

# If we know 'a' and 'g', 4 informs us of 'e'
new_aeg = string_diff('abcdefg', len_to_ptn[4][0])
new_eg = new_aeg.replace(new_a, "")
new_e = new_eg.replace(new_g, "")
lookup_original[new_e] = "e"

# 'b' and 'e' are missing twice from 2, 3 and 5
missing_235 = "".join([string_diff("abcdefg", i) for i in len_to_ptn[5]])
missing_235_no_e = missing_235.replace(new_e, "")
new_b = [s for s in 'abcdefg' if missing_235_no_e.count(s) == 2][0]
lookup_original[new_b] = "b"

# 'd' is the difference between 4 and 1 (c, f) with b
new_d = string_diff(len_to_ptn[4][0], new_b.join(len_to_ptn[2][0]))
lookup_original[new_d] = "d"

# 'c' and 'f' are left, 'f' is inside all digits of length 6
new_cf = string_diff("abcdefg", "".join(lookup_original.keys()))
cf_in_069 = [string_intresect(new_cf, i) for i in len_to_ptn[6]]
new_f = [c for c in cf_in_069 if len(c) == 1][0]
new_c = string_diff(new_cf, new_f)
lookup_original[new_f] = "f"
lookup_original[new_c] = "c"

original_pattern = ["".join(sorted([lookup_original[c] for c in o])) for o in out]

tmp = {
       'abcefg': 0,
       'cf': 1,
       'acdeg': 2,
       'acdfg': 3,
       'bcdf': 4,
       'abdfg': 5,
       'abdefg': 6,
       'acf': 7,
       'abcdefg': 8,
       'abcdfg': 9
       }

original_value = [tmp[op] for op in original_pattern]




# %%