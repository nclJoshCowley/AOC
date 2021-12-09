#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
"""


# %% Read from file
def read_from_file(path):
    with open(path, "r") as file:
        lines = file.read().split("\n")

        split = [l.split(" | ") for l in lines]
        patterns = [s[0].split(" ") for s in split]
        output = [s[1].split(" ") for s in split]

        return patterns, output


# %%
lookup_digit_length = {
    0: 6,
    1: 2,  # Unique!
    2: 5,
    3: 5,
    4: 4,  # Unique!
    5: 5,
    6: 6,
    7: 3,  # Unique!
    8: 7,  # Unique!
    9: 6
    }


def is_easy_pattern(ptn):
    easy_lens = [lookup_digit_length[i] for i in (1, 4, 7, 8)]
    ptn_lens = map(len, ptn)
    return [pl in easy_lens for pl in ptn_lens]


# %% Part (a)
def part_a(path):
    patterns, output = read_from_file(path)
    n_easy_patterns = [sum(is_easy_pattern(out)) for out in output]
    print(f"Easy values in output = {sum(n_easy_patterns)}\n")


# %%
if __name__ == "__main__":
    part_a("Q08_eg.txt")
    part_a("Q08_data.txt")
