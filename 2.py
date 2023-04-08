import os
import aocd
import numpy as np


# init
session_id = '53616c7465645f5f92f504ba453e14772fc0482c4cb0e168250b14e7f7c9dcbbeb172e556af72ab28af58bd0ac2448283d83bc61565c44ad61a30a98d7d13f1a'
aoc_id = os.getenv('AOC_SESSION',session_id)
input =  aocd.get_data(session=aoc_id, day=2, year=2022)

# Part 1
opponent_play = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
}
my_play = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3,
}
outcome = {
    'lost' : 0,
    'draw' : 3,
    'win' : 6,
}
games = [line for line in input.splitlines()]

def calcul_points(opp_choice, my_choice):
    my_points = my_play[my_choice]
    turn = opponent_play[opp_choice] - my_play[my_choice]
    if turn == 1 or turn == -2:
        result = 'lost'
    if turn == 0:
        result = 'draw'
    if turn == -1 or turn == 2:
        result = 'win'
    my_points += outcome[result]
    return my_points

my_points = [calcul_points(game[0],game[-1]) for game in games]
print(f'day 2, part 1 : {np.sum(my_points)}')

# Part 2
play = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
}
outcome = {
    'X' : 0,
    'Y' : 3,
    'Z' : 6,
}

def get_key(val):
    for key, value in play.items():
        if val == value:
            return key
        if val == 0:
            return 'C'
        if val == 4:
            return 'A'

def calcul_points(opp_choice, result):
    my_points = outcome[result]
    if result == 'X':
        my_choice = get_key(opponent_play[opp_choice] - 1)
    elif result == 'Y':
        my_choice = opp_choice
    elif result == 'Z':
        my_choice = get_key(opponent_play[opp_choice] + 1)
    else:
        pass
    my_points += play[my_choice]
    return my_points

my_points = [calcul_points(game[0],game[-1]) for game in games]

print(f'day 2, part 2 : {np.sum(my_points)}')