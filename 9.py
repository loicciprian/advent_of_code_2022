import os
import aocd
import numpy as np


# init
session_id = '53616c7465645f5f92f504ba453e14772fc0482c4cb0e168250b14e7f7c9dcbbeb172e556af72ab28af58bd0ac2448283d83bc61565c44ad61a30a98d7d13f1a'
aoc_id = os.getenv('AOC_SESSION',session_id)
input =  aocd.get_data(session=aoc_id, day=9, year=2022)

# Part 1
moves = input.splitlines()

# init
hx,hy = 0,0
tx,ty = 0,0

coord = {
    'R':(1,0),
    'L':(-1,0),
    'U':(0,1),
    'D':(0,-1)    
}

pos_visited = set()


def movement(dx,dy):
    global hx,hy,tx,ty
    
    # head movement
    hx += dx
    hy += dy
    
    #tail movement
    # if the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:
    # if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up
    if abs(hx-tx)>1 or abs(hy-ty)>1: 
        sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
        sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)
 
        tx += sign_x
        ty += sign_y   
        
for move in moves:
    direction, amount = move.split(' ')
    amount = int(amount)
    dx,dy = coord[direction]
    
    for _ in range(amount):
        movement(dx,dy)
        pos_visited.add((tx,ty))
        
# return how many positions the tail of the rope does visit at least once
print(f'day 9, part 1 : {len(pos_visited)}')


# Part 2
# init
knots = [[0,0] for _ in range(10)]

coord = {
    'R':(1,0),
    'L':(-1,0),
    'U':(0,1),
    'D':(0,-1)    
}

pos_visited = set()
pos_visited.add(tuple(knots[-1]))

def movement(dx,dy):
    global knots
    
    # head movement
    knots[0][0] += dx
    knots[0][1] += dy
    
    for i in range(1, 10):
        hx, hy = knots[i - 1]
        tx, ty = knots[i]
    
        #tail movement
        if abs(hx-tx)>1 or abs(hy-ty)>1:
            sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
            sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tx += sign_x
            ty += sign_y

        knots[i] = [tx, ty]
        
for move in moves:
    direction, amount = move.split(' ')
    amount = int(amount)
    dx,dy = coord[direction]

    for _ in range(amount):
        movement(dx,dy)
        pos_visited.add(tuple(knots[-1]))
    
print(f'day 9, part 2 : {len(pos_visited)}')