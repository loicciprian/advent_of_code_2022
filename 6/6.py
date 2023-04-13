import os
import aocd


# init
session_id = '53616c7465645f5f92f504ba453e14772fc0482c4cb0e168250b14e7f7c9dcbbeb172e556af72ab28af58bd0ac2448283d83bc61565c44ad61a30a98d7d13f1a'
aoc_id = os.getenv('AOC_SESSION',session_id)
input =  aocd.get_data(session=aoc_id, day=6, year=2022)

# Part 1

n = k = 4
while len(input[k-n:k]) > len(set(input[k-n:k])):
    k += 1
processed_char_packet = k

print(f'day 6, part 1 : {processed_char_packet}')

# Part 2
n = k = 14
while len(input[k-n:k]) > len(set(input[k-n:k])):
    k += 1
processed_char_message = k
      
print(f'day 6, part 2 : {processed_char_message}')