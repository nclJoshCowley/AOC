#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
"""

# %% Dependencies
import numpy as np
import functools
    
# %% FUNCTION: Parse tricky file into bingo calls and cards
def read_bingo_from_file(f):
    with open(f, 'r') as file:
        raw_lines = file.read()
    
    lines = raw_lines.split('\n\n')
    
    calls = lines[0].split(',')
    calls = [int(x) for x in calls]
    
    matrix_str = [l.split('\n') for l in lines[1:]]
    cards = [matrix_string_to_arr(m) for m in matrix_str]
    
    return calls, cards

# %% FUNCTION: Convert cards from raw string to a NumPy array
def matrix_string_to_arr(x):
    split_strings = [m.split(' ') for m in x]
    split_strings = [list(filter(None, s)) for s in split_strings]
    out = [[int(s) for s in l] for l in split_strings]
    
    return np.array(out)

# %% Worked example
if __name__ == '__main__':
    print("")
    calls_eg, cards_eg = read_bingo_from_file('Q04_eg.txt')


# %% FUNCTION: Check if there is a winning card and return it 
def check_win(card_list, call_list):
    for cd in card_list:
        logical_matrix = [cd == cl for cl in call_list]
        scores = functools.reduce(lambda m1, m2 : m1 | m2, logical_matrix)
        
        ratio_cols = scores.sum(axis = 0) / scores.shape[1]
        ratio_rows = scores.sum(axis = 1) / scores.shape[0]
        
        # First winner found returned, others ignored.
        if any(ratio_cols == 1) or any(ratio_rows == 1):
            return cd, scores
        
    return False        

# %% Compile all above with do-it-all function
def play_game(f):
    calls, cards = read_bingo_from_file(f)

    game_over = False
    n = 0
    
    while type(game_over) == bool: 
        n += 1
        game_over = check_win(cards, calls[:n])
    
    win_card, win_loc = check_win([game_over[0]], calls[:n])
 
    win_score = calls[n - 1] * (win_card * (1 - win_loc)).sum()
    
    print(f"Score = {win_score:5.0f}, \nCard = ")
    print(win_card, "\n")

# %% Run code on both inputs    
if __name__ == '__main__':
    play_game('Q04_eg.txt')
    play_game('Q04_data.txt')
        