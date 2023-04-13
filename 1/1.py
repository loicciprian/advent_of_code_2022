import numpy as np


# init
with open('1_input.txt', 'r') as f:
    input = f.read().strip()
    calories = [[int(cal) for cal in elf_calories.split('\n')] for elf_calories in input.split('\n\n')]

# Part 1
calories_per_elf = [np.sum(per_elf) for per_elf in calories]
print(f'day 1, part 1 : {max(calories_per_elf)}')


# Part 2
calories_per_elf.sort(reverse=True)
print(f'day 1, part 2 : {np.sum(calories_per_elf[0:3])}')