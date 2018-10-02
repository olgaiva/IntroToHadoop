#!/usr/bin/python3
# purchasesMapper.py

import sys

sales_by_category = []
for line in sys.stdin:
    line_values = line.rstrip().split('\t')
    category = line_values[3]
    price = line_values[4]

    sales_by_category.append(category + '\t' + price)

sales_by_category.sort()

for line in sales_by_category:
    print(line)
    
