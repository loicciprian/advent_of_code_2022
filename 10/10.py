import os
import aocd
import numpy as np


# init
with open("10/10_input.txt") as f:
    instructions = f.read().strip().split("\n")

# Part 1
# init
X = [1]
signal_strength = []

# programm logic
for op in instructions:
    x = X[-1]
    
    # noop operation or 1st cycle of addx operation
    X.append(x)
    n=len(X)
    if n in [20,60,100,140,180,220]:
        signal_strength.append(n*x)
    
    # 2nd cycle of addx operation
    if op[:4] == 'addx':
        x = X[-1]+int(op[5:])
        X.append(x)
        n = len(X)
        
        if n in [20,60,100,140,180,220]:
            signal_strength.append(n*x)
        
#signal_strength

print(f'day 10, part 1 : {np.sum(signal_strength)}')


# Part 2

# Cycle   1 -> ######################################## <- Cycle  40
# Cycle  41 -> ######################################## <- Cycle  80
# Cycle  81 -> ######################################## <- Cycle 120
# Cycle 121 -> ######################################## <- Cycle 160
# Cycle 161 -> ######################################## <- Cycle 200
# Cycle 201 -> ######################################## <- Cycle 240

# init
X = [1]
CRT = '#'

# programm logic
for op in instructions:
    x = X[-1]
    
    # noop operation or 1st cycle of addx operation
    X.append(x)
    n=X.index(x)
    if n in [x-1,x,x+1]:
        CRT += '#'
    else:
        CRT += '.'
    
    # 2nd cycle of addx operation
    if op[:4] == 'addx':
        x = X[-1]+int(op[5:])
        X.append(x)
        n = len(X)
        
        if n in [x-1,x,x+1]:
            CRT += '#'
        else:
            CRT += '.'
    
print(f'day 10, part 2 : \n')

a,b = 0,40
for _ in range(6):
    print(CRT[a:b])
    a+=40
    b+=40