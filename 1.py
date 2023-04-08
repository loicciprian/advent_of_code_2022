import os
import aocd
import numpy as np


# init
session_id = '53616c7465645f5f92f504ba453e14772fc0482c4cb0e168250b14e7f7c9dcbbeb172e556af72ab28af58bd0ac2448283d83bc61565c44ad61a30a98d7d13f1a'
aoc_id = os.getenv('AOC_SESSION',session_id)
input =  aocd.get_data(session=aoc_id, day=1, year=2022)

# Part 1
calories = [
    [int(cal) for cal in elf_calories.split('\n')]
    for elf_calories in input.split("\n\n")
]
calories_per_elf = [np.sum(per_elf) for per_elf in calories]

print(f'day 1, part 1 : {max(calories_per_elf)}')


# Part 2
calories_per_elf.sort(reverse=True)

print(f'day 1, part 2 : {np.sum(calories_per_elf[0:3])}')