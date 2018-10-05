#!/usr/bin/python3
# storesMapper.py

import sys

sales_by_store = []
for line in sys.stdin:
    line_values = line.rstrip().split('\t')
    location = line_values[2]
    price = line_values[4]

    sales_by_store.append(location + '\t' + price)

sales_by_store.sort()

for line in sales_by_store:
    print(line)
