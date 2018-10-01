#!/usr/bin/env/python3
# purchasesMapper.py

import sys
import insertSort

category_and_sales = []
for line in sys.stdin:
    line_values = line.rstrip().split('\t')
    values = (line_values[3], line_values[4])
    index = insertSort.insertSort(category_and_sales, values)
    category_and_sales.insert(index, values)

for (category, price) in category_and_sales:
    print(category + ' ' + price)
    
