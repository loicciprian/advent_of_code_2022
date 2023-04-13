import os
import aocd
import numpy as np


# init
session_id = '53616c7465645f5f92f504ba453e14772fc0482c4cb0e168250b14e7f7c9dcbbeb172e556af72ab28af58bd0ac2448283d83bc61565c44ad61a30a98d7d13f1a'
aoc_id = os.getenv('AOC_SESSION',session_id)
input =  aocd.get_data(session=aoc_id, day=7, year=2022)

# Part 1

filesystem = [line for line in input.splitlines()]

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.directories = {}
        self.files = []
        
    def add_directory_child(self,directory):
        self.directories[directory.name] = directory
    
    def add_file_size(self,file_size):
        self.files.append(file_size)
    
    def get_size(self):
        size = np.sum(self.files)
        for directory in self.directories:
            size += self.directories[directory].get_size()
        return int(size)
    
    def all_sizes(self, sizes=None):
        if sizes is None:
            sizes=[self.get_size()]
        for directory in self.directories.values():
            sizes.append(directory.get_size())
            directory.all_sizes(sizes)
        return sizes
    
    
root = Directory('/', None)
current = root
for k in filesystem[1:]:
    if k=='$ ls':
        continue
    elif k=='$ cd ..': # return to parent directory
        current=current.parent
    elif k.startswith('$ cd'): # current directory
        current=current.directories[k[5:]]
    elif k.startswith('dir'): # directory
        current.add_directory_child(Directory(k[4:], current))
    else: # file
        current.add_file_size(int(k.split()[0]))

sizes = root.all_sizes([root.get_size()])
min_sizes = [x if x<=100000 else 0 for x in sizes]

print(f'day 7, part 1 : {np.sum(min_sizes)}')

# Part 2
np.sum(sizes)

total_disk_space_available = 70000000
min_unused_space_needed = 30000000
max_space_to_use = total_disk_space_available - min_unused_space_needed

space_used = root.get_size()
space_to_free = space_used - max_space_to_use
space_to_free

min_to_delete = np.min([x - space_to_free if x > space_to_free else 10**6 for x in sizes])

print(f'day 7, part 2 : {min_to_delete + space_to_free}')