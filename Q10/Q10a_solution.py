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

    return lines


# %% Globals
close_to_open = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"}

close_to_score = {
    "": 0,
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137}

opens = close_to_open.values()


# %% Find corruptions but ignore incomplete lines
def check_lines(line):
    unmatched_brackets = []

    for cur_ch in iter(line):
        if cur_ch in opens:
            unmatched_brackets.append(cur_ch)
        else:
            matched_bracket = close_to_open[cur_ch]
            if matched_bracket != unmatched_brackets[-1]:
                # Early exit - return corrupted bracket
                return cur_ch
            else:
                unmatched_brackets.pop()

    # Main exit - end of line with no corruption
    return ""


# %% Calculate score
def get_score_from_file(file):
    lines = read_from_file(file)
    corrutpions = [check_lines(ln) for ln in lines]
    scores = [close_to_score[ch] for ch in corrutpions]
    return sum(scores)


# %%
if __name__ == "__main__":
    print(f"Example score = {get_score_from_file('Q10_eg.txt')}")
    print(f"Input   score = {get_score_from_file('Q10_data.txt')}")
