#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
"""


# %% Import from part (a)
from Q10a_solution import read_from_file, close_to_open, opens


# %% New globals
incomplete_score = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4}

open_to_close = {v: k for k, v in close_to_open.items()}


# %% Repurpose function to filter corrupt lines
def match_lines(line):
    unmatched_brackets = []

    for cur_ch in iter(line):
        if cur_ch in opens:
            unmatched_brackets.append(cur_ch)
        else:
            matched_bracket = close_to_open[cur_ch]
            if matched_bracket != unmatched_brackets[-1]:
                # Corrupted lines, return empty list
                return []
            else:
                unmatched_brackets.pop()

    # Incomplete lines, return unmatched brackets
    return unmatched_brackets


# %%
def get_closing_seq(unmatches):
    return [open_to_close[op] for op in reversed(unmatches)]


# %%
def calculate_score(closing_seq):
    score = 0
    for closer in closing_seq:
        score *= 5
        score += incomplete_score[closer]
    return score

# calculate_score("])}>")
# > 294


# %% Calculate score
def get_midscore_from_file(file):
    lines = read_from_file(file)

    incompletes = [match_lines(ln) for ln in lines if len(match_lines(ln)) > 0]

    close_seqs = [get_closing_seq(inc) for inc in incompletes]

    scores = [calculate_score(cseq) for cseq in close_seqs]

    return sorted(scores)[int(0.5 * (len(scores) - 1))]


# %%
if __name__ == "__main__":
    print(f"Example mid-score = {get_midscore_from_file('Q10_eg.txt')}")
    print(f"Input   mid-score = {get_midscore_from_file('Q10_data.txt')}")
