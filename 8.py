import os
import aocd
import numpy as np
import pandas as pd


# init
session_id = '53616c7465645f5f92f504ba453e14772fc0482c4cb0e168250b14e7f7c9dcbbeb172e556af72ab28af58bd0ac2448283d83bc61565c44ad61a30a98d7d13f1a'
aoc_id = os.getenv('AOC_SESSION',session_id)
input =  aocd.get_data(session=aoc_id, day=8, year=2022)

# Part 1

# put tree grid as a dataframe
tree_grid = [[int(x) for x in list(line)] for line in input.splitlines()]
tree_grid = pd.DataFrame(tree_grid)

# define is_visbile function as combination from is_visible from all 4 directions 
def is_visible_from_left(line, col):
    return max(tree_grid.iloc[line,:col]) < tree_grid.iloc[line,col]

def is_visible_from_right(line, col):
    return max(tree_grid.iloc[line,col+1:]) < tree_grid.iloc[line,col]

def is_visible_from_top(line, col):
    return max(tree_grid.iloc[:line,col]) < tree_grid.iloc[line,col]

def is_visible_from_down(line, col):
    return max(tree_grid.iloc[line+1:,col]) < tree_grid.iloc[line,col]

def is_visible(line, col):
    if line == min(tree_grid) or line == max(tree_grid) or col == min(tree_grid) or col == max(tree_grid): # edge tree
        return int(True)
    else: # middle tree
         return int(is_visible_from_left(line, col) or is_visible_from_right(line, col) or is_visible_from_top(line, col) or is_visible_from_down(line, col))

# create a new dataframe visible_trees checking all trees from tree_grid
visible_trees = tree_grid.copy()
for i in tree_grid:
    for j in tree_grid:
        visible_trees.iloc[i,j] = is_visible(i,j)
        
# sum visible_trees to get the total number of visible trees
print(f'day 8, part 1 : {np.sum(np.sum(visible_trees))}')       

# Part 2

# define tree_scenic_score function as combination of its viewing distance for all 4 directions 

def left_viewing_distance(line,col):
    distance=0
    for k in range(col-1,-1,-1):
        distance+=1
        if tree_grid.iloc[line,k] >= tree_grid.iloc[line,col]:
            return distance
    return distance

def right_viewing_distance(line,col):
    distance=0
    for k in range(col+1,max(tree_grid)+1):
        distance+=1
        if tree_grid.iloc[line,k] >= tree_grid.iloc[line,col]:
            return distance
    return distance

def top_viewing_distance(line,col):
    distance=0
    for k in range(line-1,-1,-1):
        distance+=1
        if tree_grid.iloc[k,col] >= tree_grid.iloc[line,col]:
            return distance
    return distance

def down_viewing_distance(line,col):
    distance=0
    for k in range(line+1,max(tree_grid)+1):
        distance+=1
        if tree_grid.iloc[k,col] >= tree_grid.iloc[line,col]:
            return distance
    return distance

def tree_scenic_score(line,col):
    if line == min(tree_grid) or line == max(tree_grid) or col == min(tree_grid) or col == max(tree_grid): # edge tree
        return 0
    else: # middle tree
        return left_viewing_distance(line,col) * right_viewing_distance(line,col) * top_viewing_distance(line,col) * down_viewing_distance(line,col)
    
# create a new dataframe scenic_scores checking all trees from tree_grid
scenic_scores = tree_grid.copy()
for i in tree_grid:
    for j in tree_grid:
        scenic_scores.iloc[i,j] = tree_scenic_score(i,j)

print(f'day 8, part 2 : {scenic_scores.max().max()}')