#!/usr/bin/python3
# maxByCategoryReducer.py
# Can I make this a general reducer for this type of problem??

import sys

values_dict = {}
for line in sys.stdin:
    line_values = line.rstrip().split('\t')
    category = line_values[0]
    value = float(line_values[1])
    if category in values_dict:
        values_dict[category] = max(values_dict[category], value)
    else:
        values_dict[category] = value

sorted_values_dict = sorted(values_dict.items(), key=lambda x: x[0])
for line in sorted_values_dict:
    category = line[0]
    max_val = line[1]
    print(category + ' ' + str(max_val))
