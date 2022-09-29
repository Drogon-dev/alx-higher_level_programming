#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    nset = set(my_list)
    for i in nset:
        sum += i
    return sum
