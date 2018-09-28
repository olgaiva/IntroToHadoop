#!/usr/bin/env python3
# testSetPartitioner.py

import os
import sys
import random

# Insertion sort to appropriately order test set
def insert_sort(num_list, num):
    index = 0
    if not(num_list):
        return index
    for i in range(len(num_list)):
        if num_list[i] < num:
            index = i + 1
    return index 

# Requires 3 arguments:
full_file = sys.argv[1] # File which contains full set of lines
num_lines = int(sys.argv[2]) # Size of subset
test_file_name = sys.argv[3] # Name of file which will contain subset

full_file_size = os.path.getsize(full_file)

with open(full_file, 'r') as fr:
    # Pseudo-random selection:
    # Assumes line lengths are more-or-less equal
    # Uses f.seek() to avoid iterating through huge file
    # Test set will be in same order as full file

    line_indeces = [] # Will make sure same line isn't selected twice
    test_set_lines = []
    line_index = None
    random_line = ""
    for i in range(0, num_lines+1):
        while (line_index in line_indeces):
            offset = random.randrange(0,full_file_size)
            fr.seek(offset)
            fr.readline() # Finish reading what is likely a partial line
            random_line = fr.readline() # The line I want, but could be EOF
            if not(random_line): # If EOF, go to first line
                fr.seek(0)
                random_line = fr.readline()
            line_index = fr.tell()

        order = insert_sort(line_indeces, line_index)
        line_indeces.insert(order, line_index)
        test_set_lines.insert(order, random_line)

with open(test_file_name, "w+") as fw:
    fw.write("".join(test_set_lines))
            
