#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:   Josh Cowley
@email:    j.cowley1@ncl.ac.uk
"""


# %% Dependencies
import numpy as np
import functools

from Q04a_solution import read_bingo_from_file, matrix_string_to_arr

# %% FUNCTION: Improved version of check_win()
def check_win(card_list, call_list):
    for cd in card_list:
        logical_matrix = [cd == cl for cl in call_list]
        scores = functools.reduce(lambda m1, m2 : m1 | m2, logical_matrix)
        
        ratio_cols = scores.sum(axis = 0) / scores.shape[1]
        ratio_rows = scores.sum(axis = 1) / scores.shape[0]
        
        # First winner found returned, others ignored.
        if any(ratio_cols == 1) or any(ratio_rows == 1):
            return True, cd, scores
        
    return False, cd, scores 


# %%
def play_loss_game(f):
    calls, cards = read_bingo_from_file(f)
    
    while len(cards) > 0:
        game_over = False, None, None
        n = 0
        while not game_over[0]: 
            n += 1
            game_over = check_win(cards, calls[:n])
        
        _, win_card, win_loc = check_win([game_over[1]], calls[:n])
        
        # Remove winning cards from the pool
        cards = [c for c in cards if not np.array_equal(c, win_card)]
        
        # Most recent winner gets overwritten so last winner = loser.
        loss_card = win_card
        loss_loc = win_loc

    loss_score = calls[n - 1] * (loss_card * (1 - loss_loc)).sum()
    print(f"Score = {loss_score:5.0f}, \nCard = ")
    print(loss_card, "\n")
    
# %% Run code on both inputs    
if __name__ == '__main__':
    play_loss_game('Q04_eg.txt')
    play_loss_game('Q04_data.txt')
        