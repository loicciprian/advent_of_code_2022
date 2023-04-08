import os
import aocd
import numpy as np


# init
session_id = '53616c7465645f5f92f504ba453e14772fc0482c4cb0e168250b14e7f7c9dcbbeb172e556af72ab28af58bd0ac2448283d83bc61565c44ad61a30a98d7d13f1a'
aoc_id = os.getenv('AOC_SESSION',session_id)
input =  aocd.get_data(session=aoc_id, day=3, year=2022)

# Part 1
rucksacks = [line for line in input.splitlines()]
compartments = [(rucksack[:int(len(rucksack)/2)],rucksack[int(len(rucksack)/2):]) for rucksack in rucksacks]

errors=[]
for compartment in compartments:
    k=0
    while compartment[0][k] not in compartment[1]:
        k+=1
    errors.append(compartment[0][k])
    
def priorities_value(char):
    if char.islower():
        value = ord(char) - 96 
    else:
        value = ord(char) - 38
    return value

errors_val = [priorities_value(error) for error in errors]

print(f'day 3, part 1 : {np.sum(errors_val)}')

# Part 2
badges=[]

for k in range(0,len(rucksacks)-2,3):
    i = 0
    while rucksacks[k][i] not in rucksacks[k+1] or rucksacks[k][i] not in rucksacks[k+2]:
        i+=1
    badges.append(rucksacks[k][i])
    
badges_val = [priorities_value(badge) for badge in badges]

print(f'day 3, part 2 : {np.sum(badges_val)}')