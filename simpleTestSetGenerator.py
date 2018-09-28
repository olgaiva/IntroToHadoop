#!/usr/bin/env python3
# simpleTestSetPartitioner.py

# This produces results which are closer to "true" randomness
# than testSetGenerator.py. Simpler, but much slower

import os
import sys
import random

# Requires 3 arguments:
full_file = sys.argv[1] # File which contains full set of lines
num_lines = int(sys.argv[2]) # Size of subset
test_file_name = sys.argv[3] # Name of file which will contain subset

# Implements reservoir sampling
test_set_lines = []

with open(full_file, 'r') as fr:
    test_set_lines = [fr.readline() for i in range(num_lines)]
    i = num_lines
    line = test_set_lines[-1]
    while (line):
        line = fr.readline()
        keep = random.random()
        if keep < num_lines/i:
            swap = random.randrange(0, num_lines)
            test_set_lines[swap] = line
            
with open(test_file_name, "w+") as fw:   
    fw.write("".join(test_set_lines))
