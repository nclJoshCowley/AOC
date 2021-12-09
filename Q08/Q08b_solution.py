#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
"""

# %% Dependencies
from functools import reduce
from Q08a_solution import read_from_file


# %% Globals
orig_patterns = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
                 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

# Renamed from `lookup_digit_length`
value_to_length = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}


orig_to_value = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4,
                 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}


# %% Utility functions for strings
def string_diff(s1, s2):
    s1_set = set([s for s in s1])
    s2_set = set([s for s in s2])
    return "".join(s1_set - s2_set)


def string_intresect(*args):
    string_list = list(args)
    char_sets = [set(char for char in s) for s in string_list]

    char_intersect = reduce(lambda x1, x2: x1.intersection(x2), char_sets)
    return "".join(sorted(char_intersect))


# %% Utility functions for pattern lookups
def lookup_op_by_value(*args):
    return [orig_patterns[v] for v in list(args)]


def filter_pattern_by_length(ptn_list, *args):
    lens = list(args)
    return list(filter(lambda x: len(x) in lens, ptn_list))


def filter_pattern_by_value(ptn_list, *args):
    vals = list(args)
    lens = [value_to_length[v] for v in vals]
    return filter_pattern_by_length(ptn_list, *lens)


# %% Main logic in "big" function
def get_signal_unmixer(ptn):
    # Number i is represented by one of the (mixed) patterns in
    # mixed_candidates[i]
    mixed_candidates = [filter_pattern_by_value(ptn, i) for i in range(10)]

    # Goes from mixed letter 'd' to original letter in prompt 'a'
    lookup_original = {}

    # Deduction: 'a' is the difference between signals in 7 and 1.
    mixed_to_a = string_diff(mixed_candidates[7][0], mixed_candidates[1][0])
    lookup_original[mixed_to_a] = "a"

    # Deduction: Only 'a' and 'g' are in all of 0, 2, 3 and 5
    patterns_for_023569 = filter_pattern_by_value(ptn, 0, 2, 3, 5, 6, 9)
    mixed_to_ag = string_intresect(*patterns_for_023569)
    mixed_to_g = string_diff(mixed_to_ag, mixed_to_a)
    lookup_original[mixed_to_g] = "g"

    # Deduction: Only 'a', 'd' and 'g' are in all of 2, 3 and 5
    mixed_to_adg = string_intresect(*filter_pattern_by_value(ptn, 2, 3, 5))
    mixed_to_d = string_diff(mixed_to_adg, mixed_to_ag)
    lookup_original[mixed_to_d] = "d"

    # Deduction: Difference between signals in 4 and 1 equals 'b' and 'd'
    mixed_to_bd = string_diff(mixed_candidates[4][0], mixed_candidates[1][0])
    mixed_to_b = string_diff(mixed_to_bd, mixed_to_d)
    lookup_original[mixed_to_b] = "b"

    # Deduction: The off signals in 4 are 'a', 'e' and 'g'
    mixed_to_aeg = string_diff('abcdefg', mixed_candidates[4][0])
    mixed_to_e = string_diff(mixed_to_aeg, mixed_to_ag)
    lookup_original[mixed_to_e] = "e"

    # Deduction: Signals missing from 0, 6 and 9 are 'd', 'c' and 'e'
    patterns_for_069 = filter_pattern_by_value(ptn, 0, 6, 9)
    missing_from_069 = [string_diff('abcdefg', s) for s in patterns_for_069]
    mixed_to_cde = "".join(missing_from_069)
    mixed_to_de = "".join([mixed_to_d, mixed_to_e])
    mixed_to_c = string_diff(mixed_to_cde, mixed_to_de)
    lookup_original[mixed_to_c] = "c"

    # Deduction: Given mixed signal for 'c' we can use 1 to obtain 'f'
    mixed_to_f = string_diff(mixed_candidates[1][0], mixed_to_c)
    lookup_original[mixed_to_f] = "f"

    return lookup_original


# %% Convert from mixed signals to original signals ('eg' -> 'cf' -> 1)
def convert_mixed_pattern_to_value(ptn, unmixer):
    original_chars = [unmixer[p] for p in ptn]
    original_ptn = "".join(sorted(original_chars))

    return orig_to_value[original_ptn]


# %% Combine all of above
def part_b(path):
    # All answers to be appended to this list
    output_values = []

    patterns, output = read_from_file(path)
    unmixers = [get_signal_unmixer(p) for p in patterns]

    for unmix, out in zip(unmixers, output):
        digits = [convert_mixed_pattern_to_value(o, unmix) for o in out]

        output_val = sum([(10 ** i) * v for i, v in enumerate(digits[::-1])])
        output_values.append(output_val)

    return output_values


# %%
if __name__ == "__main__":
    ovals_eg = part_b("Q08_eg.txt")
    print(f"Example output value sum = {sum(ovals_eg)}\n")

    ovals = part_b("Q08_data.txt")
    print(f"Input   output value sum = {sum(ovals)}\n")
