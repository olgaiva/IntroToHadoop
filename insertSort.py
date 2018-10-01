#!/usr/bin/env/python3
# insertSort.py

# Insertion sort to appropriately order test set
def insertSort(values_list, value):
    index = 0
    if not(values_list):
        return index
    for i in range(len(values_list)):
        if values_list[i][0] < value[0]:
            index = i + 1
    return index

