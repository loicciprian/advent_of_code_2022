import os
import aocd
import re
import numpy as np


# init
session_id = '53616c7465645f5f92f504ba453e14772fc0482c4cb0e168250b14e7f7c9dcbbeb172e556af72ab28af58bd0ac2448283d83bc61565c44ad61a30a98d7d13f1a'
aoc_id = os.getenv('AOC_SESSION',session_id)
input =  aocd.get_data(session=aoc_id, day=4, year=2022)

# Part 1
paired_sections = [line for line in input.splitlines()]
paired_sections = [[int(section) for section in re.split(r'[-,]', sections)] for sections in paired_sections] 

sections_fully_contained = [
    (section[0] <= section[2] and section[1] >= section[3]) or (section[0] >= section[2] and section[1] <= section[3])
    for section in paired_sections
]

print(f'day 4, part 1 : {np.sum(sections_fully_contained)}')

# Part 2
sections_contained = [
    section[0] in range(section[2],section[3]+1)
    or
    section[1] in range(section[2],section[3]+1)
    or
    section[2] in range(section[0],section[1]+1)
    or
    section[3] in range(section[0],section[1]+1)
    for section in paired_sections
]

print(f'day 4, part 2 : {np.sum(sections_contained)}')