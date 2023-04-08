import os
import aocd
import numpy as np
import pandas as pd


# init
session_id = '53616c7465645f5f92f504ba453e14772fc0482c4cb0e168250b14e7f7c9dcbbeb172e556af72ab28af58bd0ac2448283d83bc61565c44ad61a30a98d7d13f1a'
aoc_id = os.getenv('AOC_SESSION',session_id)
input =  aocd.get_data(session=aoc_id, day=5, year=2022)

# Part 1

# [N] [G]                     [Q]    
# [H] [B]         [B] [R]     [H]    
# [S] [N]     [Q] [M] [T]     [Z]    
# [J] [T]     [R] [V] [H]     [R] [S]
# [F] [Q]     [W] [T] [V] [J] [V] [M]
# [W] [P] [V] [S] [F] [B] [Q] [J] [H]
# [T] [R] [Q] [B] [D] [D] [B] [N] [N]
# [D] [H] [L] [N] [N] [M] [D] [D] [B]
#  1   2   3   4   5   6   7   8   9 

stacks = {
    1 : ['D','T','W','F','J','S','H','N'],
    2 : ['H','R','P','Q','T','N','B','G'],
    3 : ['L','Q','V'],
    4 : ['N','B','S','W','R','Q'],
    5 : ['N','D','F','T','V','M','B'],
    6 : ['M','D','B','V','H','T','R'],
    7 : ['D','B','Q','J'],
    8 : ['D','N','J','V','R','Z','H','Q'],
    9 : ['B','N','H','M','S']
}

rearrangement_procedure = [line for line in input[325:].splitlines()]

rearrangement_procedure = pd.DataFrame(
    [move.replace('move ','').replace(' from ',',').replace(' to ',',').split(',') for move in rearrangement_procedure],
    columns=['nb','from','to'])

for k in range(len(rearrangement_procedure)):
    # select crates to move
    to_move = stacks[int(rearrangement_procedure.iloc[k,1])][-int(rearrangement_procedure.iloc[k,0]):]
    # remove the crates from start stack
    del stacks[int(rearrangement_procedure.iloc[k,1])][-int(rearrangement_procedure.iloc[k,0]):]
    # order crates as picked up one by one
    to_move.reverse()
    # add crates to move to arrival stack
    stacks[int(rearrangement_procedure.iloc[k,2])] += to_move

last=''
for v in stacks.values():
    last+=(v.pop())

print(f'day 5, part 1 : {last}')

# Part 2
stacks = {
    1 : ['D','T','W','F','J','S','H','N'],
    2 : ['H','R','P','Q','T','N','B','G'],
    3 : ['L','Q','V'],
    4 : ['N','B','S','W','R','Q'],
    5 : ['N','D','F','T','V','M','B'],
    6 : ['M','D','B','V','H','T','R'],
    7 : ['D','B','Q','J'],
    8 : ['D','N','J','V','R','Z','H','Q'],
    9 : ['B','N','H','M','S']
}

for k in range(len(rearrangement_procedure)):
    # select crates to move
    to_move = stacks[int(rearrangement_procedure.iloc[k,1])][-int(rearrangement_procedure.iloc[k,0]):]
    # remove the crates from start stack
    del stacks[int(rearrangement_procedure.iloc[k,1])][-int(rearrangement_procedure.iloc[k,0]):]
    # no need to reverse this time ; crates are moved keeping the same order
    # to_move.reverse()
    # add crates to move to arrival stack
    stacks[int(rearrangement_procedure.iloc[k,2])] += to_move
    
last_9001=''
for v in stacks.values():
    last_9001+=(v.pop())
      
print(f'day 5, part 2 : {last_9001}')