#!/usr/bin/env/python3
# sumByCategoryReducer.py
# Can I make this a general reducer for this type of problem??

import sys

values_dict = {}
for line in sys.stdin:
    line_values = line.rstrip().split('\t')
    category = line_values[0]
    value = float(line_values[1])
    if category in values_dict:
        values_dict[category] = values_dict[category] + float(value)
    else:
        values_dict[category] = value

for category, total in values_dict.items():
    print(category + ' ' + str(total))
