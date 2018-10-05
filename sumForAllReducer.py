#!/usr/bin/python3
# sumForAllReducer.py
# Can I make this a general reducer for this type of problem??

import sys

values_dict = {"sales": 0, "total": 0}
for line in sys.stdin:
    line_values = line.rstrip().split('\t')
    value = float(line_values[1])
    values_dict["sales"] = values_dict["sales"] + 1
    values_dict["total"] = values_dict["total"] + value
    
print(values_dict["sales"])
print(values_dict["total"])
    
